print('Programa gera cinco numeros aleatórios e coloca em uma tupla. Depois mostra os números gerados e o maior e menor.')
from random import randint
# casa = []
# for a in range(5):
#     num_aleatorio = randint(1, 5)
#     casa.append(num_aleatorio)
# num = tuple(casa)

# print(f'A tupla de numeros aleatórios é {num}')
# print(f'O menor valor da lista é {sorted(num)[0]}')
# print(f'O maior valor da lista é {sorted(num)[-1]}')

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram {n}')
print(f'O maior valor sorteado foi {max(n)}')
print(f'O maior valor sorteado foi {min(n)}')
for numeros in n:
    print(f'{numeros}', end=' ')
