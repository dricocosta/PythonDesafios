'''refaça o desafio 35 dos triâgulos, acrescentando o recurso de
mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes'''

print('-='*15)
print('Analisador de Triângulos')
print('-='*15)
reta1 = float(input('Digite a primeira reta: '))
reta2 = float(input('Digite a segunda reta: '))
reta3 = float(input('Digite a terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas formam um triângulo', end=' ')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO.')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os valores digitado NÃO PODEM formar um triângulo.')

