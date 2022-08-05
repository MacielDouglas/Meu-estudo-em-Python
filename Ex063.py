print('Leia um número e mostre na tela o s n primieros elementos de uma sequencia de FIBONACCI ')

print('---'*12)
print('Sequência de Fibonacci')
print('___'*12)
num = int(input('quantos termos você quer mostrar? '))
print('~~~'*12)
c = 1
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')
while c <= num:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c = c + 1
print('FIM!!!')
