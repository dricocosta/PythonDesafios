#Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A primeira nota foi {}, a segunda nota {} e a média é {}.'.format(n1, n2, media))

print('A primeira nota foi {}, a segunda nota {} e a média é {}.'.format(n1, n2, ((n1+n2)/2)))
