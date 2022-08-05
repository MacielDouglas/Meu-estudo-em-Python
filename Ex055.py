print('Programa que leia o peso de cinco pessoas.No final, mostra qual foi o maior e o nmenor peso lidos.')

maior = 0
menor = 0
for calculo in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessooa? '.format(calculo)))
    if calculo == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))

