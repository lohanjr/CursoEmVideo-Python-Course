# Create an algorithm that reads a number and shows its double, triple, and square root

number = float(input('Enter a number: '))

double = number * 2
triplo = number * 3
squareRoot = number ** 0.5

print('Your number was: \033[1;33m{}\033[m, its double is: {:.1f}, its triple is: {:.1f} and its square root is: {:.1f}'.format(number, double, triplo, squareRoot))