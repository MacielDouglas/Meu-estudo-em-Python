print('Leia o nome completo de algume e imprime o primeiro e o ultimo nome')
nome = str(input('Digite o seu nome Completo: ')).strip().title()

print('O seu nome é: {}'.format(nome))
print('O seu primeiro nome é: {}'.format(nome.split()[0]))
print('O seu ultimo nome é: {}' .format(nome.split()[-1]))

