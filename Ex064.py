print('digite um numero, o programa soma menos o 999 que é para parar')

num = int(input('Digite um número ou 999 para parar: '))
soma = c = 0
while num != 999:
    soma += num
    num = int(input('Digite um número ou 999 para parar: '))
    c += 1
print('Você digitou {} números e soma de todos foi: {}'.format(c, soma))
