'''Faça um programa que leia um número qualquer
e mostre o seu fatorial.'''


n = int(input('Digite um número para saber seu fatorial: '))
c = n
f = 1 # Fatorial e multiplicação sempre começa com 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))
