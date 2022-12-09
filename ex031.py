'''Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas.'''

distancia = float(input('Digite a distancia percorrida em km: '))
print('Sua viagem será de {} km.'.format(distancia))
if distancia <= 200:
    print('O preço da passagem é R${:.2f}.'.format(distancia * 0.50))
else:
    print('O preço da pasagem é R${:.2f}.'.format(distancia * 0.45))
