'''escreva um programa que leia um númeor n inteiro qualquer
e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci'''

print('-' * 23)
print('Sequência de Fibonacci')
print('-' * 23)
n = int(input('Quantos termos você quer mostrar?: '))
t1 = 0
t2 = 1
print('=' * 37)
print('{} -> {}'.format(t1, t2), end='')
contador = 3
while contador <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador = contador + 1
print(' -> Fim.')
