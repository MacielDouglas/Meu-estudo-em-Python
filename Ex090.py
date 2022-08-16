print('''O programa le nome e media de um aluno guardando tbm a situação em um dicionário.
No final mostre o contreudo da estutura na tela\n''')
aluno = dict()
#aluno = {'nome': '', 'média': float(), 'situação': ''}
aluno['nome'] = str(input('Digite o nome do aluno: ')).title().strip()
aluno['média'] = float(input(f"Digite a média de {aluno['nome']}: "))

if aluno['média'] >= 7.0:
    aluno['situação'] = 'Aprovad'
else:
    aluno['situação'] = str('Reprovad')
sexo = str(input('Masculino ou Feminino [M/F}? ')).lower().strip()

if sexo == 'm':
    print(f"O aluno {aluno['nome']}, teve média de {aluno['média']}, e por isso ele está: {aluno['situação']}o!!!")
else:
    print(f"A aluna {aluno['nome']}, teve média de {aluno['média']}, e por isso ela está: {aluno['situação']}a!!!")


print('\n Método 2 \n')
estudante = dict()


