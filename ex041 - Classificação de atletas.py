'''A confederação Nacional de Natação precisa de um programa que leia o
 ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER'''

from datetime import date
nascimento = int(input('Digite o ano de Nascimento: '))
atual = date.today().year
idade = atual - nascimento

if idade <= 9:
    print('O atleta tem {} anos e sua categoria é MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('O atleta tem {} anos e sua categoria é INFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('O atleta tem {} anos e sua categoria é JUNIOR.'.format(idade))
elif idade > 19 and idade <= 25:
    print('O atleta tem {} anos e sua categoria é SÊNIOR.'.format(idade))
else:
    print('O atleta tem {} anos e sua categoria é MASTER.'.format(idade))
