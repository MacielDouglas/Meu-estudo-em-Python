print('Programa le nome e peso guarda em uma lista, no final mosta\nQuantas pessoas foram cadastradas\nlista com a mais pesadas\nLista com as mais leves\n')
pessoas = []
pesado = []
leve = []
while True:
    pessoa = []
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()
    x = str(input('Quer continuar? [S/N] ')).lower()

    if x == 'n':
        break
for lendopeso in pessoas:
    if lendopeso[1] >= 100:
        pesado.append(lendopeso[0])
    else:
        leve.append(lendopeso[0])

print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'As pessoas mais pesadas foram: {pesado}')
print(f'As pessoas mais leves foram: {leve}')

print('\nMétodo dois\n')
temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas. ')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()





