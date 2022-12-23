'''Crie um programa que leia uma frase qualquer
e diga se ela é um palindromo, desconsiderando espaços.'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split() # separa as palavras
junto = ''.join(palavra) # junta as palavras sem espaço
inverso = ''
for letra in range(len(junto)-1, -1, -1): # pega a última letra da palavra
    inverso = inverso + junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('E um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo.')

