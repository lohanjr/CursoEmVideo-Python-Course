# Create a program that reads how much money a person has in their
# wallet and shows how many dollars they can buy.
# Consider US$1 = R$3.27

amount = float(input('Enter the amount of money that you have: R$'))

print('Converting this amount to dollars, you would have: \033[1;32mUS${:.2f}\033[m'.format((amount/3.27)))