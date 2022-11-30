'''Crie um programa que leia o nome completo de uma pessoa e mostre:
1) O nome com todas as letras maiusculas e minusculas
2) Quantas letras no total (sem considerar espaços)
3) Quantas letras tem o primeiro nome'''

nome = str(input('Digite o nome completo: ')).strip()
print('Analisando o nome completo....')
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome possui em minusculas é {}.'.format(nome.lower()))

print('Seu nome tem ao todo {} letras.'.format(len(nome)-nome.count(' ')))

print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))