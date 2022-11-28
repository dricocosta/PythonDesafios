#Escreva um programa que converta uma temperatura digitada em C para F

celsius = float(input('Digite a temperatura em ºC: '))
fahrenheit = celsius * 1.8 + 32
print('A temperatura de  {}ºC é igual a {}ºF.'.format(celsius, fahrenheit))
