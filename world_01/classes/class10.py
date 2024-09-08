# CONDITIONS
grade1 = float(input('What is your first grade? '))
grade2 = float(input('What is your second grade? '))
avarage = (grade1 + grade2)/2
print('Your final avarage is: {:.1f} and the school avarage is 6.0'.format(avarage))
if avarage <= 5.9:
    print('You will have to retake your tests! :(')
else:
    print('Congrats! You are above avarage! :)')
print('--End--') # Caso um print ou qualquer outro comando nao esta alinhado ao bloco condicional, ele sempre sera executado!