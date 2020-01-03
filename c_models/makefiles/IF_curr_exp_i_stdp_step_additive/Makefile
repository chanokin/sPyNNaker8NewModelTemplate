APP = $(notdir $(CURDIR))
BUILD_DIR = build/

NEURON_MODEL = $(NEURON_DIR)/neuron/models/neuron_model_lif_impl.c
NEURON_MODEL_H = $(NEURON_DIR)/neuron/models/neuron_model_lif_impl.h
INPUT_TYPE_H = $(NEURON_DIR)/neuron/input_types/input_type_current.h
NEURON_IMPL_H = $(NEURON_DIR)/neuron/implementations/neuron_impl_standard.h
THRESHOLD_TYPE_H = $(EXTRA_SRC_DIR)/my_models/threshold_types/adaptive_threshold.h
SYNAPSE_TYPE_H = $(NEURON_DIR)/neuron/synapse_types/synapse_types_exponential_impl.h

SYNAPSE_DYNAMICS = $(NEURON_DIR)/neuron/plasticity/stdp/synapse_dynamics_stdp_mad_impl.c
TIMING_DEPENDENCE = $(EXTRA_SRC_DIR)/my_models/plasticity/stdp/timing_dependence/timing_step_impl.c
TIMING_DEPENDENCE_H = $(EXTRA_SRC_DIR)/my_models/plasticity/stdp/timing_dependence/timing_step_impl.h
WEIGHT_DEPENDENCE = $(NEURON_DIR)/neuron/plasticity/stdp/weight_dependence/weight_additive_one_term_impl.c
WEIGHT_DEPENDENCE_H = $(NEURON_DIR)/neuron/plasticity/stdp/weight_dependence/weight_additive_one_term_impl.h


include ../extra.mk
