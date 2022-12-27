#Faça um programa que leia a largura e a altura de uma parede em
# metros, calcule a sua área e quantidade de tinta necessária
# para pinta-la, sabendo que cada litro de tinta pinta uma área
# de 2m quadrados

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta = area / 2
print('A parede tem {:.2f} m² e precisa de {:.2f} lts de tinta para pintá-la.'.format(area, tinta))


