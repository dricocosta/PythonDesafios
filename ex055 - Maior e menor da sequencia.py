'''FAça um programa que leia o peso de cinco pessoas e
mostre qual foi o maior e o menor pesso lidos.'''

maiorPeso = 0
menorPeso = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('O maior peso digitado foi {}kg e o menor {}kg.'.format(maiorPeso, menorPeso))
