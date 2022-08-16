print('''Programa com uma função maior(). Que recebe vários parâmetros com valores inteitos
O programa tem que analisar todos os valores e dizer qual deles é o maior.\n''')
from time import sleep


def maior(* valores):
    num = 0
    print('-=-' * 20)
    print(f'Analizando os valores passados...')
    for x in valores:
        print(f'{x}', end=' ')
        sleep(0.3)
        if x > num:
            num = x
    print(f'Foram informados {len(valores)} ao todo.')
    print(f'O maior valor informado foi {num}')


maior(2, 9, 4, 5, 7, 1, 10)
sleep(1)
maior(4, 7, 0)
sleep(1)
maior(1, 2)
sleep(1)
maior(6)
sleep(1)
maior(0)

