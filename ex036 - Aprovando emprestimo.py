'''Escreva um programa para aprovar o emprestimo bancário para a compra
de uma casa. Pergunte o valor da casa, o salario do comprador e
em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salario ou então o emprestimo será negado'''

valorCasa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o salário do comprador: R$ '))
meses = float(input('Digite a quantidade de meses para pagar: '))

prestacao = valorCasa / meses
#prestacao = valorCasa / (anos * 12)
print('Para pagar uma casa de R${} em {} meses,'.format(valorCasa, meses), end='')
print('a prestação da casa será de R${} por mês.'.format(prestacao))

if prestacao > (salario * 30) / 100:
    print('Empréstimo recusado. A prestação excedeu 30% do salário.')
else:
    print('Empréstimo aprovado!')
