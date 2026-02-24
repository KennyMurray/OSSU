## 6.100A PSet 1: Part C
## Name: Kenneth Murray
## Time Spent: 50 minutes
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
initial_deposit = float(input("Enter the initial deposit "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
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

