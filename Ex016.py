print('Programa que leia um numero real e mostra a parte inteira')

real = float(input('Digite um número real qualquer: '))
print('o numero real é: ', int(real))

print('Outra forma seria')

from math import floor
inteiro = floor(real)

print(inteiro)
