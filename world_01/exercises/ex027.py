# Make a program that reads a person's full name and then shows the first and last name separately.
# ex... Ana Maria de Souza | 1st: Ana | Last: Souza

name = str(input('Type your full name: ')).strip()
print('Your first name is: {}'.format(name.split()[0].capitalize()))
print('Your last name is: {}'.format(name.rsplit(" ", 1)[1].capitalize()))