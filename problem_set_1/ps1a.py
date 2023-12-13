# Problem Set 1a
# https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/mit6_0001f16_ps1/
# 
# Write a program to calculate how many months it will take you to save up enough money for a down payment. 

portion_down_payment = 0.25 # percent
current_savings = 0
r = 0.04 # percent
portion_saved = 0.0
down_payment_total = 0.0

# Get input
annual_salary = input( "Enter your annual salary: " )
portion_saved = input( "Enter the percent of your salary to save, as a decimal: " )
total_cost = input( "Enter the cost of your dream home: " )

# Process
monthly_salary = float( annual_salary ) / 12
down_payment_total = float( total_cost ) * portion_down_payment
current_month = 0
isSaving = True
while ( isSaving ):
    monthly_investment_return = current_savings * r / 12
    monthly_deposit = float( monthly_salary ) * float( portion_saved )
    current_savings = current_savings + monthly_deposit + monthly_investment_return
    current_month = current_month + 1
    if ( current_savings >= down_payment_total ):
        isSaving = False

# Results
print( "Number of months:", current_month )
