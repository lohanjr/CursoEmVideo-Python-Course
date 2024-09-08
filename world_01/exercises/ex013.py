# Make an algorithm that reads an employee's salary
# and shows his new salary, with a 15% increase

salary = float(input('Enter your salary: R$'))

increase = (15/100) * salary

print('Your salary is: R${:.2f} and your new salary after 15% increase is: \033[32mR${:.2f}\033[m'.format(salary, (salary+increase)))