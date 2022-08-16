print('''Programa c/ função contador(), recebe tres parametros: inicio, fim e passo e realiza a contagem.
O programa realiza atraves da função criada: 

a) De i até 10, de 1 em 1
b) De 10 ate 0, de 2 em 2
c) uma contagem personalizada.\n''')
from time import sleep

def contador(x, y, c):
    print(f'Contagem de {x} até {y} de {c} em {c}')
    if c < 0:
        c *= -1
    if c == 0:
        c = 1

    if x < y:
        cont = x
        while cont <= y:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont += c
        print('FIM')
    else:
        cont = x
        while cont >= y:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont -= c
        print('FIM!!!')


def linha():
    print('-=-' * 15)


linha()
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
linha()
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, 2)
linha()
print('Agora é a sua vez de personalizar a contagem!!!')
linha()
num1 = int(input('Inicio: '))
num2 = int(input('Fim: '))
pas = int(input('Passo: '))

linha()
print(f'Contagem de {num1} até {num2} de {abs(pas)} em {abs(pas)}')
contador(num1, num2, pas)




