# Write a program that reads a value in meters and displays
# Converted to centimeters and millimeters

value = float(input('Type a value in meters: '))

cm = value * 100
mm = value * 1000


print('Your value was: \033[4;31m{}m\033[m and converting to kilometers: {}km, to hectometers: {}hm, to decameters: {}dam'.format(value, (value/1000), (value/100), (value/10)))
print('to decimeters: {}dm, to centimeters: {}cm and to millimeters: {}mm'.format((value*10), cm, mm))