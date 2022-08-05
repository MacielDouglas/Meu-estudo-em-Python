brasileirao = ('Palmeiras', 'Corinthias', 'Fluminense', 'Atlético Mineiro', 'Atlético Paranaense', 'Flamengo', 'Internacional', 'Bragantino', 'Santos',
               'São Paulo', 'Ceará', 'Botafogo', 'Goiás', 'Coritiba', 'América Mineiro', 'Avai', 'Cuiabá', 'Atlético Goianiense', 'Juventude', 'Fortaleza')
# print(brasileirao)
print(
    f'\nEsses são os cinco primeiros colocados da tablea {brasileirao[:5]}\n ')
print(f'Esses são os ultimos quatro colocados da tabela {brasileirao[-4:]}\n')
print(f'Essa é a lista alfabética da tabela {sorted(brasileirao)}\n')
print('O time Bragantino está na {}ª posição'.format(brasileirao.index('Bragantino')+1))
print(f'O time Bragantino está na {brasileirao.index("Bragantino") + 1}ª posição')
