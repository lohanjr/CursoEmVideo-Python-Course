# Make an algorithm that reads the price of a product
# and shows its new price, with a 5% discount

price = float(input('Enter your products price: R$'))

discount = (5/100) * price

print('The price of your product is: R${} and with a 5% discount it will be: \033[7;37mR${:.2f}\033[m'.format(price, (price-discount)))