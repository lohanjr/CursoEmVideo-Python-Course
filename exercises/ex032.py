# Make a program that reads any year and shows if it is a leap year

year = int(input('Type any year: '))
if year % 4 == 0 and year % 100 != 0:
    print('Divisible by 4 but not by 100, so it is a LEAP year!')
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print('Divisible by 4, by 100 and by 400, so it is a LEAP year!')
else:
    print('It is not a LEAP year!')