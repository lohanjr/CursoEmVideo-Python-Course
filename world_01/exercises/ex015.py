# Write a program that asks for the number of kilometers traveled by a rented car
# and the number of days for which it was rented. Calculate the price to pay, knowing that
# the car costs R$60 per day and R$0.15 per kilometer driven.

days = int(input('Write the total number of days you had the rental car: '))
distance = float(input('Write the total distance in kilometers that you drove with the rental car: '))

bill = (days * 60) + (distance * 0.15)
print('Your final bill it will cost you: \033[1;31mR${:.1f}\033[m'.format(bill))
print('\033[36mCalculated: ({} days * R$60) + ({}km * R$0.15)\033[m'.format(days, distance))