#include "timing_step_impl.h"

accum tau_plus;
accum tau_minus;

address_t timing_initialise(address_t address) {
    log_info("timing_initialise: starting");
    log_info("\tSTDP nearest-pair rule");

    // Copy LUTs from following memory
    accum *accum_address = (accum *)address;
    tau_plus = *accum_address;
    ++accum_address;

    tau_minus = *accum_address;
    ++accum_address;

    log_info("timing_initialise: completed successfully");
    return (address_t)(accum_address);
}