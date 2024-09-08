# Make a program that reads a number from 0 to 9999 and shows on the screen
# each of the separate digits, e.g. Enter a number: 192 | 1: Hundred | 9: Ten | 2: Unit

number = str(input('Type an int number between 0 and 9999: '))

if len(number) == 1:
    print('Unit: {}'.format(number))
elif len(number) == 2:
    print('Unit: {}'.format(number[1]))
    print('Ten: {}'.format(number[0]))
elif len(number) == 3:
    print('Unit: {}'.format(number[2]))
    print('Ten: {}'.format(number[1]))
    print('Hundred: {}'.format(number[0]))
elif len(number) == 4:
    print('Unit: {}'.format(number[3]))
    print('Ten: {}'.format(number[2]))
    print('Hundred: {}'.format(number[1]))
    print('Thousand: {}'.format(number[0]))
else:
    print('ERROR! Type a valid number!')
print('---END---')