#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triangulo retângulo. calcule e mostre o comprimento da hipotenusa.
'''
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hipot = (co ** 2 + ca ** 2) ** (1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(hipot))
'''

import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hipot = math.hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hipot))

