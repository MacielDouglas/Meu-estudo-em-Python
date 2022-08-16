print('''Programa tem uma função ficha(), que recebe dois paramentros opcionais:
O nome de um jogador e quantos gols ele marcou. O programa é capaz de mostrar a ficha, mesmo sem nenhum dado informado.''')


def ficha(nome, num=0):
    if nome == str():
        nome = str('< desconhecido >')
    else:
        nome = nome
    print(f'O jogador {nome} fez {num} gols(s) no campeonato')


jogador = str(input('Nome do Jogador: ')).title()
gols = str(input('Numero de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(jogador, gols)

