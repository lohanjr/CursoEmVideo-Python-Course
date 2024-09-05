# Create a program that reads any real number and shows your entire portion
# Ex: 6.127 | the number 6,127 has the integer part 6
from math import trunc

realnumber = float(input('type a float number: '))
print('The number: {} has: \033[4;31m{}\033[m as the integer part!'.format(realnumber, trunc(realnumber)))