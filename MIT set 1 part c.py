#Find rate to purchase $1M house in 36 months
#raise is 7%, annual return 4%. dwnpymt 25%

#variables
annual_salary = float(input('Enter annual salary: '))
total_cost = 1000000
semi_annual_raise = .07
r = .04/12
down_payment = .25 * total_cost
current_savings = 0

#Bisection search
num_guesses, low = 0, 0
high = 10000 # 10000 --> 100.00% --> 1
ans = (high + low)/2
epsilon = 100

#calculations
while abs(down_payment - current_savings) > epsilon:
    monthly_salary = annual_salary/12
    ans = (high + low)/2
    if ans == 10000:
        break
    current_savings = 0
    save_rate = ans/10000
    for months in range(1,37):
        roi = current_savings * r
        monthly_portion = monthly_salary * save_rate
        current_savings = current_savings + monthly_portion + roi
        if months % 6 == 0:
            monthly_salary *= (1 + semi_annual_raise)
        if current_savings > (down_payment + epsilon):
            break
    if current_savings < down_payment:
        low = ans
    else:
        high = ans
    num_guesses += 1
if ans == 10000:
    print('Cannot purchase down payment in 36 months')
else:
    print(f'Save {ans/100:.2f}% of monthly salary. Took {num_guesses} guesses') 
