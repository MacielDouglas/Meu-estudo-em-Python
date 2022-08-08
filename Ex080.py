print('''O usuario digita cinco valores numéricos e cadastreos em uma lista.
Já na posição coreta de inserção(Sem usar o sort(). No final, mostra a lista ordenada na tela.\n''')

num = []
for i in range(5):
    x = int(input('digite um numero: '))
    if x in num:
        x = int(input('Esse numero já existe, digite novamente um numero: '))

    if num == []:
        num.append(x)
    else:
        for c in range(len(num)):
            if x < num[c]:
                num.insert(c, x)
                break
            elif x > num[-1]:
                num.append(x)
                break
    # print(f'O numero {x}, foi adicionado na posição {num[c]}')
print(num)

print('Metodo dois\n')
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('+=' *30)
print(f'Os valores digitados em ordem foram {lista}')


