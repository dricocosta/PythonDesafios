'''Crie um programa que leia dois valores e mostre um menu
como o abaixo:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        multiplica = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, multiplica))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor entre {} e {} é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe novos números.')
        n1 = int(input('Digite o primeiro númro: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Encerrando o programa.')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim')
