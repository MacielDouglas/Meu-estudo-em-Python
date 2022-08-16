
jogador = dict()
jogador['nome'] = str(input('Qual o nome do jogador? ')).title()
partidas = list()
y = int(input(f'Quantas partidas {jogador["nome"]} jogou? ')) + 1
for x in range(1, y):
    partidas.append(int(input(f"Quantos gols na partida {x}? ")))
jogador['gols'] = partidas[:]
total = 0
for x in jogador['gols']:
    total += x
jogador['total'] = total
print('-==-' * 15)
print(jogador)
print('-==-' * 15)
print(f'O Campo nome tem o valor de {jogador["nome"]}')
print(f"O campo gols tem o valor de {jogador['gols']}")
print(f'O campo total tem o valor de {jogador["total"]}')
print('-==-' * 15)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
p = 0
for p in range(0, len(jogador['gols'])):
    print(f'    => Na partida {p + 1}, ele fez {jogador["gols"][p]} gols.')
print(f"Foi um total de {jogador['total']} gols")

jogador.clear()
partidas.clear()
print('\nMétodo 2\n')
jogador = dict()
partidas = list()
jogador['nome'] =str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols n apartida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'     => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
