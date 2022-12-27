#Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário com 15% de aumento.

salario = float(input('Digite o salário do funcionário R$'))
novo = salario + (salario * 15 / 100)
print('O salário de R${:.2f} teve um aumento de 15% e passou para R${:.2f}.'.format(salario,novo))
