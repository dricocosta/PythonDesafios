#Escreva um programa que converta uma temperatura digitada em C para F

celsius = float(input('Digite a temperatura em C: '))
converte = celsius * 1.8 + 32
print('A temperatura de  {} graus C é igual a {} graus Fahrenheit.'.format(celsius, converte))
