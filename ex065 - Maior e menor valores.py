'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores.'''

n = 0
media = cont = soma = maior = menor = 0
opcao = 'S'
while opcao != 'N':
    n = int(input('Digite um número inteiro: '))
    soma = soma + n
    cont = cont + 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input('Quer continuar a digitar valores? [ Digite N para sair]: ')).upper().strip()[0]
media = soma / cont
print('A média dos {} valores digitados é {:.2f}.'.format(cont, media))
print('O maior valor digitado foi {} e o menor foi {}.'. format(maior, menor))
print('Até logo.')
