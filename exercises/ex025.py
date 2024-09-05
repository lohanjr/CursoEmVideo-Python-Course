# Create a program that reads a person's name and tells them if they have 'SILVA' in their name

name = str(input('Type your full name: ')).strip()

if name.upper().count('SILVA') != 0:
    print('Nice! Your name has SILVA in it')
else:
    print('You are not a SILVA! :(')