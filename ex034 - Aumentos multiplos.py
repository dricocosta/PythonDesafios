'''Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento.
Para salários superiores a R$.1250,00 calule um aumento de 10 % e
para inferiores ou iguais, o aumento será de 15%.'''

salario = float(input('Digite seu salário R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print(novo)
else:
    novo = salario + (salario * 10 / 100)

print('Quem ganhava R${:.2f} passou a ganhar R${:.2f}.'.format(salario, novo))


