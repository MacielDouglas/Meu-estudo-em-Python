pessoas = dict()

while True:
    nome = str(input('Digite nome: ')).title()
    pessoas[nome] = {'sexo': str(input('Sexo: [M/F] ')).capitalize(),
                     'idade': int(input('Idade: '))}
    x = input('Quer continuar? [S/N] ')
    if x == 'n':
        break
print(pessoas)
idade = 0
p = 0
for x in pessoas:
    idade += pessoas[x]['idade']
    if pessoas[x]['sexo'] == 'F':
        p += 1
media = idade / len(pessoas)
print(f"- O grupo tem {len(pessoas)} pessoas.")
print(f'A média de idade é de {media:.2f} anos')


print(idade)
print(p)
print('F' in pessoas[nome]['sexo'])
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

print('Metodo 2')
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).title()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro!!! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro!!! Por favor digite apenas M ou F.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastrads.')
media = soma / len(galera)
print(f'A média de idade é de {média:5.2f} anos')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('D Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='' )
            print()
print('<<< ENCERRADO >>>')

print(pessoa)
print(galera)


