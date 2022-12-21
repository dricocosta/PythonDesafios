'''Desenvolva um programa que leia SEIS números inteiros e mostre
a soma apenas daqueles que forem pares. Se o valor digitado for ímpar,
desconsidere-o'''

soma = 0
cont = 0
for n in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} números PARES e a soma entre eles foi {}.'.format(cont, soma))
