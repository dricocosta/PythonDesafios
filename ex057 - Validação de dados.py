'''Façla um programa que leia o sexo de uma pessoa,
mas só aceite os calores "M" ou "F". Caso esteja errado,
peça a digitação novamente até ter um valor correto.'''

'''
sexo = ''
while sexo != "M" and sexo != "F":
    nome = str(input('Digite seu nome: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    if sexo != "M" and sexo != "F":
        print("Inválido. Digite novamente.")
    else:
        print('Seu nome é {} e você é do sexo {}.'.format(nome, sexo))
        print('Fim!')
'''
# Simplificado
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
