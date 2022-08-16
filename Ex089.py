print('''Programa que leia nome e duas notas de vários alunos e guarda tudo em uma lista composta.
No final, mostra um boletim contendo a média de cada um e permita que o usuário possa:
Mostrar as notas de cada aluno individualmente.\n''')

print('Notas dos alunos')
alunos = []
x = 's'
while True:
    while x != 'n':
        notas = []
        numeros = []
        if x == 's':
            notas.append(str(input('Digite o nome do aluno(a): ')))
            numeros.append(float(input((f'Digite a primeira nota do {notas[0]}: '))))
            numeros.append(float(input(f'Digite a segunda nota de {notas[0]}: ')))
            notas.append(numeros)
            alunos.append(notas)
            x = str(input('Quer continuar? [S/N] ')).lower()
        else: 
            break
    print('-=' *30)
    for x in range(len(alunos)):
        media = (alunos[x][1][0] + alunos [x][1][1]) / 2
        print(f'{x} {alunos[x][0]} {media}')
    while True:
        x = int(input(f'Mostrar nota de qual aluno? (999, interrompe): '))
        if x != 999:
            print(f'O aluno(a): {alunos[x][0]}, tirou as seguintes notas: {alunos[x][1]}')
        else:
            break
    break
print('=-'*30)
print('Fim!!!!!')

print('\n')
print('Oção numero dois\n')
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('--' * 30)
print(f'{"Nº.":<4}{"NOME":<15}{"MÉDIA":>8}')
print('-' *26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<15}{a[2]:>8.1f}')
while True:
    print('-' *35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando....')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('Obrigado e Volte Sempre...')
