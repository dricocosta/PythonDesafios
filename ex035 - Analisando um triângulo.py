'''Desenvolva um programa que leia o comprimento de trÊs retas e diga
 ao usuário se elas podem ou não formar um triângulo.'''

print('-='*15)
print('Analisador de Triângulos')
print('-='*15)
reta1 = float(input('Digite a primeira reta: '))
reta2 = float(input('Digite a segunda reta: '))
reta3 = float(input('Digite a terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta2 and reta3 < reta1 + reta2:
    print('Os valores digitados PODEM formar um triângulo.')
else:
    print('Os valores digitado NÃO PODEM formar um triângulo.')

