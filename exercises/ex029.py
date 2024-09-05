# Write a program that reads the speed of a car. If it exceeds 80km/h,
# show a message saying that it has been fined. The fine will cost R$7/km over the limit

speed = int(input('What is cars speed? '))
if speed <= 80:
    print(f'Your speed is: {speed}km/h and it is out of the 80km/h limit!')
else:
    print(f'Your speed is: {speed}km/h and it is inside the 80km/h limit!')
    print(f'Fined! The fines cost is: R${(speed-80)*7}')