# The same teacher from the previous challenge wants to draw the order of presentation
# of the students' work. Make a program that reads the names of the four students and shows the order drawn

from random import shuffle

students = input('Enter the name of your 4 students, separating them with a single space: ').split()

print('Your list of 4 students is: {}'.format(students))
shuffle(students)
print('And the presentation order will be: {}'.format(students))