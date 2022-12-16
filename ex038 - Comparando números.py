'''Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O PRIMEIRO valor é maior que o segundo.')
elif n2 > n1:
    print('O SEGUNDO valor é maior que o primeiro.')
else:
    print('Não existe valor maior. Os dois são iguais.')
