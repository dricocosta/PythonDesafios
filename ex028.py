'''Escreva um programa que faça o computador sortear um numero inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador.

O programa deverá escrever na tela se o usuário acertou ou errou.'''

from random import randint
from time import sleep
n = int(input('Advinhe que numero vou sortear: '))

#Faz o computador sortear um número:
sorteado = randint(0, 5)

# Adiciona pausa de 3 segundos pra revelar o valor
print('Processando...')
sleep(3)

#Condição:
if n == sorteado:
    print('Você acertou! O numero sorteado foi {}'.format(sorteado));
else:
    print('Você errou. O numero sorteado foi {}.'.format(sorteado))
print('FIM.')
