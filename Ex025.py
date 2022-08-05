print('Ler o nome da pessoa e ver se tem a palavra Silva')

silva = str(input('Digite o seu nome completo: ')).strip()
print('Voce tem a palavra Silva no seu nome?', 'silva' in silva.lower())