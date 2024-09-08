# Make a program that reads a sentence and shows:
# How many times does the letter 'A' appear;
# In what position it first appears;
# In which position it appears for the last time.

name = str(input('Type your full name: ')).upper().strip()

print('The letter A appears {}x in your full name'.format(name.count('A')))
print('The letter A appears for the first time in the position: {}'.format(name.find('A')+1))
print('The letter A appears for the last time in the position: {}'.format(name.rfind('A')+1))