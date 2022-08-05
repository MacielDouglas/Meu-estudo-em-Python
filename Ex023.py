print('Programa que leia de 0 a 9999 e mostre na tela cada um dos digitos separados')

entrada = input('Digite um numero de 0 a 9999: ')
print('unidade: ', entrada[3])
print('dezena: ', entrada[2])
print('centena: ', entrada[1])
print('milhar: ', entrada[0])

print('Fazendo de forma matemática')
num = int(input('Digite novamente um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analizando o numero {}.....'.format(num))
print('Unidade: {}' .format(u))
print('Dezena: {}' .format(d))
print('Centena: {}' .format(c))
print('Milhar: {}' .format(m))