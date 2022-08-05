print('Programa para calcular quantidade de tintas')

alt = float(input('Qual a altura em metros da parede: '))
lar = float(input('Qual a largaura em metros da parede: '))
parede = alt * lar
tinta = parede / 2

print('A parede tem: {:.2f} metros, será necesário: {:.2f} litros de tinta'.format(parede, tinta))

