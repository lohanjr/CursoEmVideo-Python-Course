# Make a program that reads the length and height of a wall in meters,
# calculates its area and the amount of paint needed to paint it,
# knowing that each liter of paint paints an area of ​​2m²

length = float(input('Enter the length of your wall in meters: '))
high = float(input('Enter the high of your length in meters: '))

print('The total area of your wall is: \033[4m{}\033[mm²'.format((length*high)))
print('And you will need: \033[33m{}L\033[m of paint to paint your wall'.format((length*high)/2))