'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é
a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag).'''

n = 0
contador = 0
soma = 0
n = int(input('Digite um número [999 PARA PARAR]: '))
while n != 999:
    contador = contador + 1
    soma = soma + n
    n = int(input('Digite um número [999 PARA PARAR]:  '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(contador, soma))
