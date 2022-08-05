print('Progrma ler um numero e diz se é par ou impar')

num = int(input('Digite um numero inteiro qualquer: '))
n = num %2
if n == 0:
    print('Você digitou um número PAR')
else:
    print('Voce digitou um número IMPAR')
