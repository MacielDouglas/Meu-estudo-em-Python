print('Tabuda em Loop, interrompido quando valor negativo...')

num = 0
while True:
    num = int(input('Digite um número para saber sua tabuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        num1 = num * c
        print(f'A tabuada de {num} é {num} x {c} = {num1}')
        print(f'{num} x {c} = {num*c}')
print('\nPrograma Tabuada encerada!!!')




