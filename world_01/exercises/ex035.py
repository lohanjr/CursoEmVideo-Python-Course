# Develop a program that reads the length of three lines 
# and tells the user whether or not they can form a triangle

a = float(input('Enter the length of the first line: '))
b = float(input('Enter the length of the second line: '))
c = float(input('Enter the length of the third line: '))
if a + b > c and a + c > b and b + c > a:
    print('\033[34mThe lines could form a triangle!\033[m')
else:
    print('\033[35mIt could NOT form a triangle :(\033[m')
print('Your lines lengths were: a: {:.1f}, b: {:.1f} and c: {:.1f}'.format(a, b, c))