print('Leia o nome e preço de produtos. \n')
print("====="*10)
print('------' * 3, end='')
print(' LOJA BARATOS ', end='')
print('------' * 3)
print('====='*10)
nome = nome1 = ''
menor = preco2 = total = float()

while True:
    nome = str(input('Qual o nome do produto: ')).upper().strip()
    preco = float(input(f'Qual o valor pago pelo {nome}: '))
    total += preco
    if preco >= 1000:
        preco2 += 1
    if menor == 0:
        menor = preco
        nome1 = nome
    if menor > preco:
        nome1 = nome
        menor = preco

    continua = str(input('Quer cadastrar mais? [S/N]: ')).upper().strip()[0]
    while continua != 'S' and continua != 'N':
        continua = str(input('Quer cadastrar mais? [S/N]: ')).upper().strip()[0]

    if continua == 'N':
        print('---------- FIM DO PROGRAMA ----------')
        print(f'O total da compra foi R$ {total}')
        print(f'Temos {preco2:.0f} produto(s) custanto mais de R$ 1.000,00')
        print(f'O produto mais barato foi {nome1}, custanto R$ {menor:.2f}')
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))

