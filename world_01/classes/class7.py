# ARITHMETIC OPERATORS:
# + Addition
# - Subtraction
# / Division
# * Multiplication
# ** Exponentiation
# // Integer division
# % Remainder.

# Order of precedence
# 1 - ()
# 2 - **
# 3 - * , / , // e %
# 4 - + e -

# Practicing
# Mask alignment
name = input('What is your name? ')
print('Nice to meet you {:=^20}!'.format(name))

n1 = int(input('Type a number from 1 to 5: '))
n2 = int(input('Type another number from 1 to 5: '))
addition = n1 + n2
subtraction = n1 - n2
division = n1 / n2
intDivision = n1 // n2
remainder = n1 % n2
exponentiation = n1 ** n2
print('Results between them: addition = {}, subtraction = {}, division = {}'.format(addition, subtraction, division))
print('int divison = {}, resto = {} and exponentiation = {}'.format(intDivision, remainder, exponentiation))