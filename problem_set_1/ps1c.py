# Problem Set 1c
# https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/mit6_0001f16_ps1/
# 
# You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in
# 36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of
# the required down payment.
#
# Note: bisection search is a requirement

portion_down_payment = 0.25 # percent
r = 0.04 # percent
down_payment_total = 0.0
moms_gift = 100
total_cost = 1000000
semi_annual_raise = 0.07
lower_bound = 0
upper_bound = 10000
maximum_time_in_months = 36

# Get input
annual_salary = input("Enter your annual salary: ")

# Process
loop_count = 0
while ( True ):
    current_savings = 0
    test_portion = ( upper_bound + lower_bound ) / 2
    portion_saved = float( test_portion ) / 10000
    monthly_salary = float( annual_salary ) / 12 
    down_payment_total = float( total_cost ) * portion_down_payment
    current_month = 0
    isSaving = True
    while ( isSaving ):
        if ( 0 < current_month and 0 == ( current_month % 6 ) ):
            monthly_salary = monthly_salary + ( monthly_salary * semi_annual_raise )
        monthly_investment_return = float( current_savings ) * r / 12
        monthly_deposit = monthly_salary * float( portion_saved )
        current_savings = current_savings + monthly_deposit + monthly_investment_return
        if ( current_savings >= down_payment_total - moms_gift ):
            isSaving = False
        if ( current_month > maximum_time_in_months ):
            isSaving = False
        if ( isSaving ):
            current_month = current_month + 1
    if ( current_month < maximum_time_in_months ):
        upper_bound = test_portion - 1
    if ( current_month > maximum_time_in_months ):
        lower_bound = test_portion + 1
        if ( 10000 < lower_bound ):
            print( "It is not possible to pay the down payment in three years.")
            break
    if ( current_month == maximum_time_in_months ):
        print( "Best savings rate:", int( test_portion ) / 10000 )
        print( "Steps in binary search", loop_count + 1 )
        break
    if ( loop_count > 16 ):
        break
    loop_count = loop_count + 1
