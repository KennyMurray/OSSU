## 6.100A PSet 1: Part B
## Name: Kenneth Murray
## Time Spent: 10 minutes
## Collaborators: None

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter yearly salary: "))
portion_saved = float(input("How much of your salary you saved: "))
cost_of_dream_home = float(input("Cost of dream house: "))
semi_annual_raise = float(input("Enter your semi-annual raise: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
monthly_salary = yearly_salary/12
portion_down_payment = 0.25
amount_saved = 0
r = 0.05
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved < (cost_of_dream_home*portion_down_payment):
    amount_saved += (amount_saved*(r/12))
    amount_saved += (monthly_salary*portion_saved)
    months += 1
    if months%6 == 0:
        yearly_salary += (yearly_salary * semi_annual_raise)
        monthly_salary = yearly_salary/12
    
print(f"Number of months: {months}")