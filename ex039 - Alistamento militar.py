'''Escreva um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é hora de se alistar ou se já
passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de seu nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))

if idade == 18:
    print('É hora de se alistar!!!')
elif idade > 18:
    saldo = idade - 18
    alistamento = atual - saldo
    print('Você deveria ter se alistado a {} anos.'.format(saldo))
    print('Seu alistamento foi em {}'.format(alistamento))
elif idade < 18:
    saldo = 18 - idade
    print('Faltam {} anos para se alistar.'.format(saldo))

