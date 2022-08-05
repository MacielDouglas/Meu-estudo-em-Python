print('Programa, lê dois numeros ineiros e compareos, mostrando mansagem qual deles é o maior.')

num = int(input('Digite o primeiro numero para comparação: '))
num2 = int(input('Digite o segundo numero pra comparação: '))

if num > num2:
    print('O primeiro numero: {}, é maior que o segundo número: {}.'.format(num, num2))
elif num2 > num:
    print('O segundo número: {}, é maior que o primeiro número: {}.'.format(num2, num))
else:
    print('Os números são exatamente iguais: {}.'.format(num))
