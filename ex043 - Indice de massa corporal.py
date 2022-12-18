'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu statu, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- Acima de 40: Obesidade mórbida'''

print('Índice de Massa Corporal')
print('=*='*20)

peso = float(input('Digite seu peso: (kg)  '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura * altura)
print('Seu IMC é {:.0f}.'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL.')
elif imc >= 25 and imc < 30:
    print('Você está com Sobrepeso.')
elif imc >= 30 and imc <= 40:
    print('Você está com Obesidade.')
else:
    print('Você está com Obesidade mórbida.')
