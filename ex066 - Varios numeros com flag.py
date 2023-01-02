'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar 999, que é a
condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles.'''

soma = contador = 0
while True:
    num = int(input('Digite um número inteiro [999 para Parar]: '))
    if num == 999:
        break
    soma = soma + num
    contador = contador + 1
print(f'A soma dos {contador} números digitados foi {soma}.')
