# A teacher wants to draw one of his four students to erase the blackboard.
# Make a program that helps him, reading their name and writing the name of the chosen one

from random import choice

students = input('Enter the name of your 4 students, separating them only by a single space: ').split()

print('Your list of 4 students is: {}'.format(students))
print('The chosen was: {}'.format(choice(students)))