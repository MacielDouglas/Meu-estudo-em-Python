print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo.\nCalcule e mostre o comprimento da hipotenusa')

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

from math import hypot
h3 = hypot(co, ca)
print(h3)

import math
h2 = math.hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(h2))
