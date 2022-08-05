print('Prgo, leia o primeiro termo e a razão de uma Progressão Aritimética. No final mostra os 10 primeiros termos dessa progressão')

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input('Digite o segundo numero: '))
pulo = int(input('Digite o numero de contagem: '))
y = int()

for x in range(1, 11, pulo):
    y = y + num1
print(y)
print(x)
print(range)

print('Método correto:\n')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='-> ')
print('ACABOU!')






