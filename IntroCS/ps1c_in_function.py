def part_c(initial_deposit):
	#########################################################################
	
	cost_of_dream_home = 800000
	portion_down_payment = 0.25
	down_payment = cost_of_dream_home*portion_down_payment
	r = 0.0
	months = 36
	steps = 0
	amount_saved = initial_deposit*(1+r/12)**months
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	
	max_r = 1
	min_r = 0
	while (abs(amount_saved - down_payment)>100):
	    steps += 1
	    if steps == 20:
	        break
	    if amount_saved < down_payment:
	        min_r = r
	    if amount_saved > down_payment:
	        max_r = r
	    r = (min_r + max_r) / 2
	    if r == 0.0:
	        break
	    if r > 0.999:
	        r = None
	        break
	    amount_saved = initial_deposit*(1+r/12)**months
	    
	print(f"Best savings rate: {r}")
	print(f"Steps in bisection search: {steps}")
	
	return r, steps