print('Leia o sexo de uma pessoa, mas so aceite valores M ou F. Caso esteja errado peça valor novamente')
# sexo = 'M' or 'F'
sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = input('Escolha o sexo M/F: ')
        
print('FIM')

print('Método 2')
sx = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sx not in 'MmFf':
    sx = str(input('Dados inválidos; Por favor, infome seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} validado com sucesso'.format(sx))
