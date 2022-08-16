print('Cria uma matriz de dimensao 3x3 e prencha os valores')
extrutura = []
for i in range(0, 3):
    for x in range(0, 3):
        valor = int(input(f'Digite um valor para [{i},{x}]: '))
        extrutura.append(valor)
print(extrutura)
print(f'[ {extrutura[0]} ][ {extrutura[1]} ][ {extrutura[2]} ]')
print(f'[ {extrutura[3]} ][ {extrutura[4]} ][ {extrutura[5]} ]')
print(f'[ {extrutura[6]} ][ {extrutura[7]} ][ {extrutura[8]} ]')

print('\n Método 2: ')
matriz = [[0, 0, 0], [0, 0, 0],  [0, 0, 0]]
for linha in range(0, 3):
    for casa in range(0, 3):
        matriz[linha][casa] = int(input(f'Digite um valor para [{linha}, {casa}]: '))
print('-=' * 30)
for linha in range(0, 3):
    for casa in range(0, 3):
        print(f'[{matriz[linha][casa]:^5}]', end='')
    print()
