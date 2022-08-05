print('Descobrir se um numero é primo')

num = int(input('Digite um numero para saber se ele é um número primo: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('. O número {} foi divisível {} vezes.'.format(num,tot))
if tot == 2:
    print('O número {}, é um número primo'.format(num))
else:
    print('O número {}, não é um número primo'.format(num))


