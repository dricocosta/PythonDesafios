'''Jogo da advinhação'''

from random import randint
print('Vamos jogar. Tente advinhar o número que estou pensando.')
computador = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite: '))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente.')

print('Você acertou com {} tentativas.'.format(palpite))

