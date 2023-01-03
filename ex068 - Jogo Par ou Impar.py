'''Faça um programa que faça par ou impar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
v = 0
while True:
    jogador = int(input('Digite um número inteiro: '))
    computador = randint(0,10)
    total = jogador + computador
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar? [ P/I ]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}.')
    print('DEU PAR!' if total % 2 == 0 else 'DEU IMPAR')
    if opcao == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif opcao == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!!')
            v += 1
        else:
            print('VocÊ PERDEU!')
            break
        print('Vamos jogar novamente.')
print('-' * 30)
print(f'GAME OVER. Você venceu {v} vezes')
print('-' * 30)


