primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da progressão: '))
termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        contador = contador + 1
    print('PAUSA')
    mais = int(input('''Quantos termos você quer mostrar a mais? 
    Para encerrar, digite [ 0 ]: '''))
print('Progressão finalizada com {} termos mostrados.'.format(total))
