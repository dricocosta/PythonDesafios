'''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o númeor solicitado for negativo'''

while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    print(f'TABUADA DE {num}')
    for c in range(1, 11):
        print(f'{c} x {num} = {c * num}')
    print('-' * 20)
print('Programa encerrado. Volte sempre.')
