# Write a program that makes the computer 'think' of an integer between 0 and 5
# and ask the user to try to figure out what the number the computer chose.
# The program should write on the screen whether the user lost or won

from random import randint
num = randint(0,5)
x = int(input('Pick a number between 0 and 5: '))
if x == num:
    print('Wow! You won! You guessed the random number! Congrats!')
else:
    print('What a pity, you lost! You did not guess the random number.')
print(f'The random number was: {num}')