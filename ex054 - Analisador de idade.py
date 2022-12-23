'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e
quantas já são maiores.'''

from date19time import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano a {}ª pessoa nasceu:: '.format(c)))
    idade = atual - ano
    if idade >= 18:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('Ao todo {} pessoas são maiores de idade e {} são menores de idade.'.format(totmaior, totmenor))


