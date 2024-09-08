# Develop a program that asks the distance of a trip in Km.
# Calculate the price of the ticket, charging R$0.50/km for trips
# of up to 200km and R$0.45 for longer trips

distance = float(input('How far is your trip in Km? '))
if distance <= 200:
    print('Your tickets cost will be: R${:.2f} (calculated R$0,50/km)'.format(distance*(1/2)))
else:
    print('Your tickets cost will be: R${:.2f} (calculated R$0,45/km)'.format(distance*0.45))