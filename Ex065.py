print('MAior e menor valores')

num1 = num2 = num3 = num4 = int(input('digite um número: '))
c = str(input('Quer continuar? [S/N]')).lower().strip()

while c != 'n':
    num3 = int(input('digite um número: '))
    num4 += num3
    if num1 < num3:
        num1 = num3

    if num2 > num3:
        num2 = num3

    c = str(input('Quer continuar? ')).lower().strip()
print(c)
print(num4)
print('O maior valor digitado foi {} e o menor {}'.format(num1, num2))



print('----Metodo dois 2 -----')
resp = 's'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor - num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))



