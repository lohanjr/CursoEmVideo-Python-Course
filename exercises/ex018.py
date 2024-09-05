# Make a program that reads any angle and shows it on the screen:
# the value of the sine, cosine, and tangent of that angle
from math import sin, cos, tan, radians

x = float(input('Type any angle: '))

print('Your angle is: {} your sine is: {:.3f}, your cosine: {:.3f} and your tangent: {:.3f}'.format(x, sin(radians(x)), cos(radians(x)), tan(radians(x))))