# Primitive types and data outputs

# How to find out the primitive type of an input
n1 = input('Type anything: ') # input naturalmente vem como string
print('type:',type(n1)) # <class 'str'>
print('---END---')

n2 = int(input('Enter a number: ')) # converte input para tipo integer
print('type (converting to int):',type(n2)) # <class 'int'>
print('---END---')

# Extra Challenge / Using mask '{}' in the print message to be used by the '.format()' method
num1 = int(input('Enter a number from 1 to 5: '))
num2 = int(input('Enter anohter number from 1 to 5: '))
addition = num1 + num2
print('The addition of {} and {} is: {}'.format(num1, num2, addition))