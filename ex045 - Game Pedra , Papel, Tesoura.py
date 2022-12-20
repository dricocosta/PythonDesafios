'''Crie um jogo que faça o computador jogar JOKENPÔ com você.'''


from random import randint
from time import sleep
opcao = ('Pedra', 'Papel', "Tesoura")
computador = randint(0, 2)
print('''Escolha a opção que quer jogar:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Digite sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('*-'* 13)
print('Você jogou {}.'.format(opcao[jogador]))
print('O computador jogou {}.'.format(opcao[computador]))
print('*-'* 13)

if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE.')
    elif jogador == 2:
        print('COMPUTADOR VENCE.')
    else:
        print('JOGADA INVÁLIDA.')

elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE.')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE.')
    else:
        print('JOGADA INVÁLIDA.')

elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE.')
    elif jogador == 1:
        print('COMPUTADOR VENCE.')
    elif jogador == 2:
        print('EMPATE.')
    else:
        print('JOGADA INVÁLIDA.')