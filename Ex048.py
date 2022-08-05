print('Soma entre todos os numeros impares que são multiplos de tres e que se encontra no intervalo 1 ate 500')



soma = 0
cont = 0
for c in range(1, 501, 2): # o 2 fará que o laço for começe a contagem no numero 1 e vai pulando de dois em dois.
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
      #  print(c, end=' ')
print(soma)
print('A Quantidade de numeros somados foi de:', cont)
