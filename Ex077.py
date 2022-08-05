palavras = ('Escola', 'Do', 'Serviço', 'De', 'Pioneiro', 'Banco', 'Brasil', 'Seguro', 'Auto')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')