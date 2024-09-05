# Create a program that reads a person's full name and shows:
# The name with all uppercase and lowercase letters;
# How many letters in total it has (without considering spaces);
# And how many letters the first name has.

name = str(input('Type your full name: ')).strip()
print('In uppercase letters: {}'.format(name.upper()))
print('In lowcase letters: {}'.format(name.lower()))
print('Numbers of letters in your full name: {} letters'.format(len(name.replace(" ", ""))))
print('Numbers of letters in your first name: {} letters'.format(len(name.split()[0])))