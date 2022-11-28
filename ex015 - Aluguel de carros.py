#Escreva um programa que pergunte a quantidade de KM percorridos por um carro
#e a quantidade de dias pelos quaisele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$60.00 por dia e R$0.15 por KM rodado.

km = float(input('Digite a distância percorrida em KM: '))
dias = float(input('Digite a quantidade de dias alugado: '))
preco = km * 0.15 + dias * 60.00
print('O preço a pagar por {} dias alugados e {} km rodados é R${:.2f}.'.format(dias, km, preco))

