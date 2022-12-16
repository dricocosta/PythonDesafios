'''Escreva um programa que leia um número inteiro e peça
para o usuário escolher qual seria a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

numero = int(input('Escreva um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] convertrer para HEXADECIMAL''')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print('A conversão de {} para binario é {}.'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('A conversão de {} para octal é {}.'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('A conversão de {} para hexadecimal é {}.'.format(numero, hex(numero)))
else:
    print('Opção inválida. Tente novamente.')