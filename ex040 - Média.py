'''Crie em programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final de acordo com a médiaatingida:
- Médid abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print('Sua média foi {:.1f}. Você foi REPROVADO.'.format(media))
elif media >= 7.0:
    print('Parabéns! Sua média foi {:.1f} e você foi APROVADO!'.format(media))
else:
    print('Sua média foi {:.1f}. Você está em RECUPERAÇÃO.'.format(media))
