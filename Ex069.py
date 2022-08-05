print('Leia a idade o sexo e pergunte se quer cadastar mais ou não')

print('\nCADASTRE UMA PESSOA')
print('----'*10)

sexo = sim = ''
maior = homem = mulher = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo != 'M' and sexo !='F':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1

    sim = str(input('Quer continuar? [S/N] ')).upper()[0]
    while sim != 'S' and sim != 'N':
        sim = str(input('Quer continuar? [S/N] ')).upper()[0]
    if sim == 'N':
        print(f'Total de pessoas com mais de 18 anos: {maior}')
        print(f'Ao todo temos {homem} homens cadastradsos')
        print(f'E temos {mulher} mulheres com menos de 20 anos')

        break


print('Opção dois')

tot18 = totH = totM20 = 0
while True:
    idad = int(input('Idade: '))
    sex = ''
    while sex not in 'MF':
        sex = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idad >= 18:
        tot18 += 1
    if sex == 'M':
        totH += 1
    if sex == 'F' and idad < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrado')
print(f'E temos {totM20} mulheres com menos de 20 anos')


