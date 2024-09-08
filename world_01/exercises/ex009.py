# Make a program that reads any integer and
# displays its multiplication table on the screen

num = int(input('Write a number from 0 to 10 to see your multiplication table: '))

print('The multiplication table of {} is:'.format(num))

for i in range(0, 11): # Retorna um objeto que produz uma sequência de inteiros desde o início(inclusivo) e o final(exclusivo)
    result = num * i
    print('{} x {:2} = \033[4;36m{}\033[m'.format(num, i, result))