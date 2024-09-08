# Make a program that reads three numbers and shows which is the BIGGEST and which is the SMALLEST

n1 = int(input('Type the first number: '))
n2 = int(input('Type the second number: '))
n3 = int(input('Type the third number: '))
namesList = [n1, n2, n3]
namesList.sort()
print('The SMALLEST number typed by you was: {}'.format(namesList[0]))
print('The BIGGEST number typed by you was: {}'.format(namesList[2]))