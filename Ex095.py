jogador = dict()
partidas = list()
time = list()

# Ler os dados de vários jogadores
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas { jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if resp == 'N':
        break

# Cabeçalho
print('-=-' * 20)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

# Resultados dos dados.
print('-=-' * 25)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=-' * 20)

# Qual dado mostrar?
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 p/ parar) '))
    if busca == 999:
        breakr
    if busca >= len(time):
        print(f'Erro! Não existe o jogador com esse código {busca}!')
    else:
        print(f' -- Levantamento do jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-=-' * 15)
print('<<<<< VOLTE SEMPRE >>>>>>')




