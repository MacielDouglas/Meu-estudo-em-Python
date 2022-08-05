print('Tabuada usando laço for')
num = int(input('Digite um numero para saber a sua tabuada: '))
print('A tabuada de {} é:'.format(num))
for x in range(1, 11):
    y = num * x
    print('{} x {} = {}'.format(num, x, y))


print('Maneira dois')
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))