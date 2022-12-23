'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média da idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos'''

somaIdade = 0
mediaIdade = 0
idadeHomemVelho = 0
nomeHomemVelho = ''
totMulherNova = 0
for c in range(1, 5):
    print('-----{}ª PESSOA-----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade = somaIdade + idade
    if c == 1 and sexo in 'Mm':
        idadeHomemVelho = idade
        nomeHomemVelho = nome
    if sexo in 'Mm' and idade > idadeHomemVelho:
        idadeHomemVelho = idade
        nomeHomemVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulherNova = totMulherNova + 1
mediaIdade = somaIdade / 4
print('A idade média do grupo é de {} anos.'.format(mediaIdade))
print('O homem mais velho do grupo tem {} anos e se chama {}.'.format(idadeHomemVelho, nomeHomemVelho))
print('O total de mulheres com menos de 20 anos é {}.'.format(totMulherNova))
