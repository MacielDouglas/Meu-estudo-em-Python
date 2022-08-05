print('O professor quer sortear uma lista de apresentação entre 4 alunos')

import random
n1 = input('Digite o primeiro aluno: ')
n2 = input('Digite o segunto aluno: ')
n3 = input('Digite o terceiro aluno: ')
n4 = input('Digite o quarto aluno: ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(lista)

from random import shuffle
shuffle(lista)
print(lista)
