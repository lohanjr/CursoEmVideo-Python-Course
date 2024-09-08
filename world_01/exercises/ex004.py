# Make a program that reads something through the keyboard and shows on the screen its primitive type
# and all possible information about it

something = input('Enter something:')
print('\033[32m-The primitve type of your enter was: \033[m',type(something))

print('Your enter contains only numbers? ', something.isnumeric())
print('Your enter contains only letters? ', something.isalpha())
print('Your enter contains letters/numbers? ', something.isalnum())
print('Your enter contains only uppercase letters? ', something.isupper())
print('Your enter contains only lowcase letters? ', something.islower())
print('Your enter is capitalized? ', something.istitle())
print('Your enter contains only spaces? ', something.isspace())