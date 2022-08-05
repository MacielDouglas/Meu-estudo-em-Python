print('Leia o nome de alguem, o nome maiusculo, minusculo, quantas letra, quantas letras primeiro nome')

nome = str(input('Digite o seu nome completo: ')).strip()

print(nome.upper())
print(nome.lower())
print('O nome {}, tem {} letras' .format(nome, len(nome) - nome.count(' ')))
print('O primeiro nome {}, tem {} letras.'.format(nome.split()[0], len(nome.split()[0])))
