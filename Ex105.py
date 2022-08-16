print('''Programa com função notas() recebe várias notas de alulnos e vai retornando um dicionário com as as seguinter informções:
Quantidade de notas, A maior nota, A menor nota, a média da turma, a situação(opc)\n''')


def notas(*n, sit=False):
    '''
    => Função para analisar notas e situaçãoes de vários alunos.
    :param n: uma ou mais notoas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['media'] = 'RUIM'
    return r


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
