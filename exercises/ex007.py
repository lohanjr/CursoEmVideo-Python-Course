# Develop a program that reads both notes
# of a student, calculate and show your average

note1 = float(input('Enter your first note: '))
note2 = float(input('Enter your second note: '))

avarage = (note1 + note2)/2

print('Your notes were: {} and {} and its avarage is: \033[1;36m{}\033[m'.format(note1, note2, avarage))