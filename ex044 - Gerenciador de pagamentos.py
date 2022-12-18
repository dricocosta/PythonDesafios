'''elabore um programa que calcule o valor a ser pago por em uma compra
considerando o seu preço normal e condição de pagamento:
- à vista Dinheiro/Cheque: 10% de Desconto
- à vista Cartão: 5% de Desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' Lojas Paris Texas '))
preco = float(input('Digite o preço das compras R$ '))
pagamento = int(input('''Digite a condição de pagamento:
[ 1 ] Á vista Dinheiro ou Cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão 
Digite sua opção: '''))

if pagamento == 1:
    total = preco - (preco * 10 / 100)
elif pagamento == 2:
    total = preco - (preco * 5 / 100)
elif pagamento == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2 parcelas de R${:.2f}.'.format(parcela))
elif pagamento == 4:
    total = preco + (preco * 20 / 100)
    totparcela = int(input('Digite a quantidade de parcelas: '))
    parcela = total / totparcela
    print('Sua compra será parcelada em {} parcelas de R${:.2f}.'.format(totparcela, parcela))
else:
    total = preco
    print('Opção inválida de pagamento. Tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco, total))
