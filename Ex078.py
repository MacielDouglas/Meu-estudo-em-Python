print('Prog. 5 valores numéricos, lista, mostre o maior e o menor valor em suas posiçoes')

num = list()
for c in range(0, 5):
  num.append(int(input('Adicione um número: ')))
maior =  0
for posicao, valor in enumerate(num):
    if maior <= valor:
        maior = valor
        pmaior = posicao
        menor = maior
    elif menor >= valor:
        menor = valor
        pmenor = posicao
    if num.count(maior) > 1:
        pmaior2 = num.index(maior, pmaior)

print('quantas veses aparece o', num.count(maior))
print('valor de a', valor)
print(f'Os numeros digitados foram: {num}')
print(f'O maior valor digitado foi {maior}, na posição: {pmaior} {pmaior2 if pmaior2 != 0 else ""}')
print(f'O menor valor digitado foi {menor}, na posição: {pmenor}')

print()
print("Método 2:")
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c} ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digirado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O maior valor digitado foi {men}, nas posiçoes ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()