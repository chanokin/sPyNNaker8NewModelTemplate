#ifndef _ADAPTIVE_THRESHOLD_TYPE_H_
#define _ADAPTIVE_THRESHOLD_TYPE_H_

#include <neuron/threshold_types/threshold_type.h>

typedef struct threshold_type_t {
    REAL threshold_value;
    REAL base_value;
    REAL increment;
    REAL decay;
} threshold_type_t;

static inline bool threshold_type_is_above_threshold(state_t value,
        threshold_type_pointer_t threshold_type) {

    bool above = REAL_COMPARE(test_value, >=, threshold_type->threshold_value);

    REAL value = threshold_type->threshold_value;
    REAL base = threshold_type->base_value;
    if (above){
        value += threshold_type->increment;
    }
    else {
        value = base + (value - base) * threshold_type->decay;
    }

    threshold_type->threshold_value = value;

    return above
}

#endif // _ADAPTIVE_THRESHOLD_TYPE_H_
