print('''Digite vários valores numericos, cadastre em um alista. E Se o número já exista, ele não será adicionado.
NO final, serão exibidos todos os valores únicos digitados, em ordem crescente\n''')

num = []
x = 's'
while x != 'n':
    valor = int(input('Digite um numero: '))
    if valor in num:
        print('Esse número já está cadastrado')
    else:
        num.append(valor)
    x = input('Quer continuar [S/N]? ').lower()
print(f'Os valorers digitados foram {sorted(num)}.\n')

print('Solução 2')
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não sderá adicionado....')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
print('-=' *30)
numeros.sort()
print(f'Você digitou os valores {numeros}')


