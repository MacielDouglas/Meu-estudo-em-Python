print('Classificação Triangulos')
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    if n1 == n2 == n3:
        print('Esse é um triangulo Equilátero, todos os seus lados são iguais')
    elif n1 == n2 != n3 or n2 == n3 != n1 or n1 == n3 != n2:
        print("Esse é um triangulo 'Isósceles', pois tem dois lados iguais")
    else:
        print('Esse é um triangulo Escaleno, todos os lados diferente')
else:
    print('Não é um triangulo')

