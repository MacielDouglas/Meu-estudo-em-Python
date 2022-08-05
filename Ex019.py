print('Professor quer sortear um aluno entre 4 alunos')

aluno01 = input('Digite o primeiro aluno: ')
aluno02 = input('Digite o segundo aluno: ')
aluno03 = input('Digite o terceiro aluno: ')
aluno04 = input('Digite o quarto aluno: ')

lista = [aluno04, aluno02, aluno03, aluno01]

from random import choice
escolhido = choice(lista)
print(escolhido)
