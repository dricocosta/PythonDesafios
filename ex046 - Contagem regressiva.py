'''FAça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artifício, indo de 10 à 0, com uma
pausa de 1 segundo entre eles.'''

from time import sleep
print('Contagem iniciada...')
for c in range (10, -1, -1):
    print(c)
    sleep(0.5)
print('\033[1:36mBUM! BUM! BUM\033[m')