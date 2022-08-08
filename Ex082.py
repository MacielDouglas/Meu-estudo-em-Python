print('''Leia vários números e coloque em um lista. Depois crie duas listas extras que vão conter:
Valores pares e impares digitados respectivametne.
No final mostre o conteudo das tres listas.\n''')
lista = list()
x = 's'
while x != 'n':
    lista.append(int(input('Digite um valor: ')))
    x = str(input('Deseja continuar? [S/N]: ')).lower()

par = []
impar = []
for x in range(len(lista)):
    if lista[x] % 2 == 0:
        par.append(lista[x])
    else:
        impar.append(lista[x])
print(f'A lista completa é: {lista}')
print(f'A lista com os números pares é: {par}')
print(f'A lista com os números impares é: {impar}')

print('\n Método dois\n')
num = list()
pares = list()
impares = list()
while True:
    num.append((int(input('Digite um número: '))))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
