# Create a program that reads an int number and shows on the screen whether it is ODD or EVEN. 
number = int(input('Type any integer number: '))
if number % 2 == 0:
    print('Your number is EVEN!')
else:
    print('Your number is ODD!')