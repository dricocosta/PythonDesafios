'''Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão
Aritmética. No final, mostre os 10 primeiros termos dessa progressâo.'''

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da progressão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('Fim.')
