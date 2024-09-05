# Write a program that takes a temperature given in degrees Celsius
# and converts it to degrees Fahrenheit.

celsius = float(input('Enter a temperature in degrees Celsius: '))
fahrenheit = (celsius * (9/5)) + 32

print('{:.1f} degrees Celsius is: {:.1f} degrees Fahrenheit!'.format(celsius, fahrenheit))