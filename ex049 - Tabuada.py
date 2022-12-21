'''Refaça o desafio 009, mostrando a tabuada de um números que o usuário
escolher, só que agora utilizando um laço for.'''

print('TABUADA')
num = int(input('Digite um número para ver sua tabuada: '))
print('-'*20)
for t in range(1, 11):
    print('{} x {:2} = {}'.format(num, t, num*t))
print('-'*20)