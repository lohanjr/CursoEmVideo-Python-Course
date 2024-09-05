# Make a program that reads an int number and shows on screen your successor and your predecessor

number = int(input('Enter an int number: '))
successor = number + 1
predecessor = number - 1
print('Your number was: \033[32m{}\033[m and its successor: {} and its predecessor is: {}'.format(number, successor, predecessor))