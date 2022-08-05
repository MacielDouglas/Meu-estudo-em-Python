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
