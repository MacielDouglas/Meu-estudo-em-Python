print('Prog leia 4 valores teclado e guarda em uma tupla. no final mostra: ')

user = []
total = 0
for c in range(0, 5):
    user.append(int(input('Digite um valor inteiro: ')))
num = tuple(user)
num.count(9)
tres = 'Não foi encontrado o numero tres.'
num2 = []

for cont in num:
    total += cont
    if cont % 2 == 0:
        num2.append(cont)
    if cont == 3:
        tres = str(f'O valor tres apareceu na {num.index(3) + 1} posição')
par = tuple(num2)

print(f'\nVocê digitou os valores {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
print(tres)
print(f'O total da soma desses numeros é: {total}')
print(f'Os numeros pares digitados são: {par}')




