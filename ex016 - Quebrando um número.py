#Crie um programa que leia um número real qualquer pelo teclado
#e mostre na telaa sua porção inteira.

'''
from math import trunc
numero = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(numero, trunc(numero)))
'''

numero = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(numero, int(numero)))
