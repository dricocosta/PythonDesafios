#Crie um programa que leia quanto dinheiro uma pessoa tem e
# mostre quantos dólares ela pode comprar. Considere USS1,00 = 3,27

real = float(input('Digite o valor que você tem na carteira? R$  '))
#dolar = real / 3.27
print('Você tem {} reais e pode comprar {:.2f} dolares'.format(real, (real/3.27)))
