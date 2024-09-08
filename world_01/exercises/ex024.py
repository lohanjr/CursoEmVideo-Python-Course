# Create a program that reads the name of a city and says if
# it begins or does not begin with the name 'SANTO'

city = str(input('Type a city name: ')).strip()

if city.upper().find('SANTO') == 0:
    print('The citys name starts with SANTO!!')
else:
    print('Not SANTO in the start! :(')