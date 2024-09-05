from math import sqrt # Importando modulos e bibliotecas
from random import random, randint # ctrl + espace -> mostra todas as funcionalidades

num = int(input('Enter a number: '))
print('Your number is: {} and its square root is: {:.1f}'.format(num, sqrt(num)))
print('Random float number (0 to 1): {:.3f} \nAnd random int number (from 1 to 5) from machine: {}'.format(random(), randint(1,5)))