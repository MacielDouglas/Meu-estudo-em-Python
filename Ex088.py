print("""Programa com palpites da Mega Sena.
O programa pergunta quantos jogos serao gerados e sorteia:
6 numero entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta\n""")
from random import randint
from time import sleep
print('-' *30)
print("     Palpites Aleatórios     ")
print('-'*30)
jogo = []
palpites = int(input('Quantos jogos voce quer?: '))
print(f'Sorteando os {palpites} jogos...')
sleep(2)

for x in range(palpites):
    valor = list()
    for y in range(6):
        #valor = list()
        num = randint(1, 60)
        if num not in valor:
            valor.append(num)
        else:
            num = randint(1, 60)
            valor.append(num)
        valor.sort() 
    print(f'Jogo {x +1}: {valor}')
    sleep(1)
print('Fim...')


print('\nMétodo 2:')
lista = list()
jogos = list()
print('-=-'*20)
quant = int(input('Quantos jogos você quer que sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('criando os numeros....')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')



