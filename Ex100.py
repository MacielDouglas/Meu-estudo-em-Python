print('''Programa tem uma lista chamada numeros e duas funções chamada sorteio() e somarPar()
A primeira vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores PARES sorteados pela função anterior\n''')
num = list()
from random import randint
from time import sleep


def sorteio():
    print('Sorteando os 5 valores da lista temos: ', end='')
    for x in range(0, 5):
        num.append(randint(0, 10))
        print(f'{num[x]}', end=' ')
        sleep(0.6)
    print('PRONTO!!!')


def par():
    pares = 0
    sorteio()
    for x in range(0, 5):
        if num[x] % 2 == 0:
            pares += num[x]
    print(f'Somando os valores pares de {num}, temos: {pares}')


par()


print('\n Metodo 2\n')

def sorteia(lista):
    print('Sorteacon 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Pronto!!!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor %2 == 0:
            soma += valor
        print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)