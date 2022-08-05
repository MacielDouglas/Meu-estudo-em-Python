print('Leia um número qualquer e mostre o seu fatorial')

from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))


num = int(input('Digite um número para calcular seu Fatorial: '))
c = num
f = 1 #fatorial = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c # mesmo que "f = f * c"
    c -= 1
print(f)

print('O fatorial de {} é {}'.format(num, f))
