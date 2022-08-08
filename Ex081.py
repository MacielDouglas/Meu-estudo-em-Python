print('''Leia vários números e coloqueos em umalista. Depois mostre:
a) Quantos números foram digitados;
b) A lista de valores ordanada de forma decrescente
c) Se o valor 5 foi digitado e está ou não na lista.\n''')

num = []
x = 's'
while x != 'n':
    num.append(int(input('Digite um valor: ')))
    x = str(input('Deseja continuar? [S/N]: ')).lower()
print(f'Voce digitou {len(num)} elementos')
print(f'Os valores em ordem decrescente é {sorted(num, reverse=True)}')
if 5 in num:
    print(f'O valor 5 faz parte da lista')
else:
    print('O valor 5 não está na lista')

print('Método 2\n')
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' *30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')




