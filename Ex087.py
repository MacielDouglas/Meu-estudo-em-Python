print('''Cria uma matriz de dimensao 3x3 e prencha os valores
a) A Soma de todos os valores pares digitados
b) A Soma dos valores da terceira coluna
c) O maior valor da segunda linha\n''')

extrutura = []
for i in range(0, 3):
    for x in range(0, 3):
        valor = int(input(f'Digite um valor para [{i},{x}]: '))
        extrutura.append(valor)
print(extrutura)
pares = 0
for p in extrutura:
    if p % 2 == 0:
        pares += p

maior = 0
if extrutura[3] > extrutura[4] and extrutura[3] > extrutura[5]:
    maior = extrutura[3]
elif extrutura[4] > extrutura[3] and extrutura[4] > extrutura[5]:
    maior = extrutura[4]
else:
    maior = extrutura[5]

print(f'[ {extrutura[0]:^5} ][ {extrutura[1]:^5} ][ {extrutura[2]:^5} ]')
print(f'[ {extrutura[3]:^5} ][ {extrutura[4]:^5} ][ {extrutura[5]:^5} ]')
print(f'[ {extrutura[6]:^5} ][ {extrutura[7]:^5} ][ {extrutura[8]:^5} ]')
print(f'A soma de todos os números pares é: {pares}')
print(f'A soma dos valores da terceira coluna é: {extrutura[2]+extrutura[5]+extrutura[8]}')
print(f'O maior valor da segunda linha é: {maior}')


print('\n Método 2: ')
matriz = [[0, 0, 0], [0, 0, 0],  [0, 0, 0]]
saopares = maior = somacoluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')

        if matriz[linha][coluna] % 2 == 0:
            saopares += matriz[linha][coluna]


    print()
print('-=' * 30)
print(f'A soma dos valores pares é: {saopares}.')
for linha in range(0 ,3):
    somacoluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somacoluna}.')

for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é: {maior}.')
