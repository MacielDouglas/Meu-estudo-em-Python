print('Crie programa que lia vários números inteiros. o programa para quando digitar 999, mostra auntos numeros foram digitados e a soma deles.')
num = soma = contador = 0
while num != -1:
    soma += num
    num = int(input('Digite um numero, ou 999 para sair : '))
    if num == 999:
        break
    contador += 1
print(f'A soma dos {contador} valores, o total de valores são {soma}')


print('\nMetodo dois\n')
sm = cont = 0
while True:
    numero = int(input('Digite um valor (999 para parar): '))
    if numero == 999:
        break
    cont += 1
    sm += numero
print(f'A soma dos {cont} valores foi {sm}!')


