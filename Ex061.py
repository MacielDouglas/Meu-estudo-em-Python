print('leia o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressaõ usando while')


print('Programa gerador de PA')
print('=-='*18)
num1 = int(input("Digite o primeiro termo: "))
num2 = int(input('Digite a razão da PA: '))

c = 0
pa = 0
print('O resultado da razâo da PA: {} como termo: {} é:'.format(num1, num2))
print('{} , '.format(num1), end='')
while c <= 8:
    pa = num1 + num2
    num1 = pa
    c = c + 1

    print('{}'.format(pa), end='')
    print(' , ' if c <= 8 else ' , FIM!!!', end='')
print('\n')


print('Método 2 dois')
primeiro = int(input('Insiro o primeiro o termo: '))
razao = int(input('Raza da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(' {} -->'.format(termo), end='')
    termo += razao
    cont +=1
print(' FIM!!!')

