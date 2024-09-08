# Make a program that reads the length of the opposite leg and the adjacent leg
# of a right triangle, calculate and show the length of the hypotenuse

leg1 = float(input('Enter the value of the first leg: '))
leg2 = float(input('Enter the value of the second leg: '))

squarehypotenuse = (leg1**2) + (leg2**2)
print('With the sum of the squares of the legs, which are: {:.2f} + {:.2f}'.format((leg1**2),(leg2**2)))
print('We have the square of the hypotenuse:  {}, resulting in the value of the hypotenuse: \033[1;35m{:.2f}\033[m'.format(squarehypotenuse, squarehypotenuse**(1/2))) # '** 1/2' calcula a raiz quadrada