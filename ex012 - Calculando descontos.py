#Faça um algorítmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.

preco = float(input('Digite o preço do produto: R$ '))
novopreco = preco - (preco * 5 / 100)

print('O produto custava R${:.2f} e com 5% de desconto vai custar R${:.2f}'.format(preco, novopreco))



