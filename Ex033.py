print('Prog lê três numeros e mostra qual é o maior e o menor')
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

maior = ''
if n1 > n2:
    if n1 > n3:
        print ('O numero n1 é o maior numero')
if n2 > n1:
    if n2 > n3:
        print('O numero n2 é o maior numero')
if n3 > n1:
    if n3 > n2:
        print('O maior numero é o n3')

print('Menor numero')
if n1 < n2:
    if n1 < n3:
        print ('O numero n1 é o menor numero')
if n2 < n1:
    if n2 < n3:
        print('O numero n2 é o menor numero')
if n3 < n1:
    if n3 < n2:
        print('O menor numero é o n3')

# Método 2
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

