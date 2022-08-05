lista = ('Caderno', 11.90, 'Lapis', 3.55, 'Borracha', 4.99, 'Estojo',
         8.76, 'Fichário', 18.99, 'Mochila', 75.87, 'régua', 10.00)

print('Lista de preços')

for cont in range(0, len(lista)):
    if cont % 2 == 0:
        produtos = lista[cont]
        cont = cont + 1
        valor = float(lista[cont])
        print(f'{produtos}............R$ {valor:.2f}')

print('----------------------------------\n')
print('METODO DOIS')

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('-' * 40)

