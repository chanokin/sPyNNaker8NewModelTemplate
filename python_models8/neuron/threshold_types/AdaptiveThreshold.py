from data_specification.enums import DataType
from pacman.executor.injection_decorator import inject_items
from spynnaker.pyNN.models.neuron.threshold_types import AbstractThresholdType
import numpy


_THRESHOLD_TAU = "tau_threshold"
_THRESHOLD_VALUE = "v_threshold"
_THRESHOLD_BASE = "base_v_thresh"
_THRESHOLD_UP = "w_threshold"
_THRESHOLD_DOWN = "v_decay"

_UNITS = dict(
    _THRESHOLD_TAU = "mS",
    _THRESHOLD_VALUE = "mV",
    _THRESHOLD_BASE = "mV",
    _THRESHOLD_UP = "",
    _THRESHOLD_DOWN = "",
)

class AdaptiveThreshold(AbstractThresholdType):
    """An adaptive threshold based on
       https://www.frontiersin.org/articles/10.3389/fncom.2018.00074/full
       It behaves as a leaky integrator of the output spikes
    """

    def __init__(self, v_thresh, v_increase, tau, v_rest):
        super(AdaptiveThreshold, self).__init__([
            DataType.S1615, # v_thresh
            DataType.S1615, # base (min v_thresh)
            DataType.S1615, # v increment {~weight} (val >= 1; mult [thresh - v_rest])
            DataType.S1615, # decay (0 < val <= 1;  mult * value)
        ])

        self._value = v_thresh
        self._v_base = v_thresh
        self._tau = tau
        self._v_increase = v_increase
        self._v_rest = v_rest

    @property
    def v_threshold(self):
        return self._value

    @v_threshold.setter
    def v_threshold(self, x):
        self._value = x

    @property
    def base_v_thresh(self):
        return self._v_base

    @base_v_thresh.setter
    def base_v_thresh(self, x):
        self._v_base = x

    @property
    def w_threshold(self):
        return self._v_increase

    @w_threshold.setter
    def w_threshold(self, x):
        self._v_increase = x

    @property
    def tau_threshold(self):
        return self._tau

    @tau_threshold.setter
    def tau_threshold(self, x):
        self._tau = x


    def get_n_cpu_cycles(self, n_neurons):
        # Calculate (or guess) the CPU cycles
        return 50 * n_neurons

    def add_parameters(self, parameters):
        # Add initial values of the parameters that the user can change
        parameters[_THRESHOLD_VALUE] = self.v_threshold
        parameters[_THRESHOLD_TAU] = self.tau_threshold
        parameters[_THRESHOLD_UP] = self.w_threshold
        parameters[_THRESHOLD_BASE] = self.base_v_thresh

    def add_state_variables(self, state_variables):
        state_variables[_THRESHOLD_VALUE] = self.v_threshold

    @inject_items({"ts": "MachineTimeStep"})
    def get_values(self, parameters, state_variables, vertex_slice, ts):
        # Return, in order of the struct, the values from the parameters,
        # state variables, or other
        tsfloat = float(ts) / 1000.0
        decay = lambda x: numpy.exp(-tsfloat / x)  # noqa E731
        toWeight = lambda x: x * numpy.abs(self.v_threshold - self._v_rest)
        return [state_variables[_THRESHOLD_VALUE],
                parameters[_THRESHOLD_BASE],
                parameters[_THRESHOLD_UP].apply_operation(toWeight),
                parameters[_THRESHOLD_TAU].apply_operation(decay)]


    def update_values(self, values, parameters, state_variables):
        (_v_thresh, _, _, _) = values
        state_variables[_THRESHOLD_VALUE] = _v_thresh

    def has_variable(self, variable):
        return variable in _UNITS

    def get_units(self, variable):
        return _UNITS[variable]
