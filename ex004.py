#Faça um programa que leia algo pelo teclado e mostre
# o seu tipo primitivo e todas as informações possíveis sobre ele.
a = input('digite algo: ')
print('Você digitou {}'.format(a))
print('Só tem espaço?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alphanumérico?', a.isalnum())
print('Está em minuscula?', a.islower())
