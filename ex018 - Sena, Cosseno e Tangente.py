#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
# tangente desse ângulo.

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que deseja calcular: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ãngulo de {} tem o SENO {:.2f}.'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO {:.2f}.'.format(angulo, cosseno))
print('O angulo de {} tem a TANGENTE {:.2f}.'.format(angulo, tangente))
