print('Leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares, se o valor digitado for ímpar desconsidere-o')
x = int()
for a in range(1, 7):
    num = int(input('Digite o {} número: '.format(a)))
    if num % 2 == 0:
        x = x + num
print('A soma de todos os números pares digitados é:', x)

print('Método 2')
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    soma += num
    cont += 1
print('Voce informou {} números e a sooma foi {}'.format(cont, soma))