'''Esva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.'''

velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Você excedeu a velocidade permitida e foi multado em R${:.2f}.'.format((velocidade - 80) * 7))
    #multa = (velocidade - 80) * 7
    #print('Você receberá uma multa de R${}.'.format(multa))
else:
    print('Você está dentro do limite de velocidade. Boa viagem!')
