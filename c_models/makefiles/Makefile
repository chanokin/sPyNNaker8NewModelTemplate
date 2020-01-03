MODELS = IF_curr_exp_i \
         IF_curr_exp_i_stdp_step_additive \
         IF_curr_exp_i_stdp_step_multiplicative




all:
	for d in $(MODELS); do $(MAKE) -C $$d || exit $$?; done

clean:
	for d in $(MODELS); do $(MAKE) -C $$d clean || exit $$?; done
