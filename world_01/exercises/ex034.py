# Write a program that asks for an employee's salary and calculates
# the amount of their raise. For salaries over R$1,250, calculate a 10% increase.
# For lower or equal, 15%.

salary = float(input('Type your salary: R$'))
increase10 = (10/100) * salary
increase15 = (15/100) * salary
if salary <= 1250:
    print('You received a 15% salary increase. Your final salary is: R${:.2f}'.format(increase15+salary))
else:
    print('You received a 10% salary increase. Your final salary is: R${:.2f}'.format(increase10+salary))