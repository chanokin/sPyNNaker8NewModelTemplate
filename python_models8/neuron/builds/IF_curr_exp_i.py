# A PyNN Model for standard neurons built from components
from spynnaker.pyNN.models.neuron import AbstractPyNNNeuronModelStandard
# Components from main tools
from spynnaker.pyNN.models.neuron.input_types import InputTypeCurrent
from spynnaker.pyNN.models.neuron.synapse_types import SynapseTypeExponential
from spynnaker.pyNN.models.defaults import default_initial_values
from spynnaker.pyNN.models.neuron.neuron_models.neuron_model_leaky_integrate_and_fire import NeuronModelLeakyIntegrateAndFire
from python_models8.neuron.threshold_types.AdaptiveThreshold import AdaptiveThreshold

class IF_curr_exp_i(AbstractPyNNNeuronModelStandard):
    
    @default_initial_values({"v_init", "isyn_exc", "isyn_inh"})
    def __init__(self,
                 # neuron model parameters and state variables
                 i_offset=0.0,
                 v_init=-70.0,
                 v_rest=-70.0,
                 v_reset=-100.0,
                 tau_m=10.0,
                 cm=2.0,
                 tau_refrac=3.0,

                 # threshold type parameters
                 v_threshold=-10.0,
                 tau_threshold=120,
                 w_threshold=1.8,

                 # synapse type parameters
                 tau_syn_E=5.0,
                 tau_syn_I=5.0,
                 isyn_exc=0.0,
                 isyn_inh=0.0
     ):
        if v_init is None:
            v_init = v_rest

        self.__v_init = v_init
        self.__v_threshold = v_threshold
        self.__tau_threshold = tau_threshold
        self.__w_threshold = w_threshold

        neuron_model = NeuronModelLeakyIntegrateAndFire(v_init, v_rest, tau_m, cm, i_offset, v_reset, tau_refrac)
        synapse_type = SynapseTypeExponential(tau_syn_E, tau_syn_I, isyn_exc, isyn_inh)
        input_type = InputTypeCurrent()
        threshold_type = AdaptiveThreshold(v_threshold, w_threshold, tau_threshold, v_rest)
        
        super(IF_curr_exp_i, self).__init__(
            model_name="IF_curr_exp_i",
            binary="IF_curr_exp_i.aplx",
            neuron_model=neuron_model,
            input_type=input_type,
            synapse_type=synapse_type,
            threshold_type=threshold_type
        )
    
    @property
    def v_init(self):
        return self.__v_init

    @v_init.setter
    def v_init(self, v_init):
        self.__v_init = v_init
   

    @property
    def v_threshold(self):
        return self.__v_threshold

    @v_threshold.setter
    def v_threshold(self, v_threshold):
        self.__v_threshold = v_threshold
        
        
    @property
    def tau_threshold(self):
        return self.__tau_threshold

    @tau_threshold.setter
    def tau_threshold(self, tau_threshold):
        self.__tau_threshold = tau_threshold
        
        
    @property
    def w_threshold(self):
        return self.__w_threshold

    @w_threshold.setter
    def w_threshold(self, w_threshold):
        self.__w_threshold = w_threshold
        
