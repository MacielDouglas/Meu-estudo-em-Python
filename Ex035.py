print('Exercicios adicione tres retas e vê se elas podem formar um triangulo.')

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 + n2 > n3:
    if n2 + n3 > n1:
        if n3 + n1 > n2:
            print('Sim é possivel formar um triangulo')
else:
    print('Não é possivel formar tringulo.')

print('-='*20)
print('metodo 2')
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('\033[31mOs seguimentos acima, Podem formar um triangulo')
else:
    print('Os seguimentos acima, não podem formar um trinagulo.')