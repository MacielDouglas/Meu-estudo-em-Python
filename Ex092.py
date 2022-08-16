print('''Leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário.
Se por acaso a CTPS for diferente de zero, o dicionário receberá tbm o ano de contratação e o salário.
Calcule e acrescente além da idade, com quantos anos a pessoa vai se aposentar.\n''')
from datetime import date
pessoa = {
    'nome': '',
    'idade': '',
    'carteira trabalho': ''}

pessoa['nome'] = str(input('Digite o nome: ')).strip().title()

hoje = date.today()
today = date.today()
aniver = []
aniver.append(int(input('Digite o dia que voce nasceu: ')))
aniver.append(int(input('Digite o mes que voce nasceu: ')))
aniver.append(int(input('Digite o ano de nascimento: ')))

if aniver[1] < today.month or aniver[1] == today.month and aniver[0] <= today.day:
    idade = date.today().year - aniver[2]

else:
    idade = (date.today().year - aniver[2]) - 1

pessoa['idade'] = idade
carteira = str(input('Voce tem carteira de trabalho? [S/N] ')).lower()
if carteira == 'n':
    pessoa['carteira trabalho'] = 'Sem Carteira'
    print(f"\nO nome tem valor de {pessoa['nome']} .")
    print(f"A idade tem valor de {pessoa['idade']} anos.")
    print('Não tem carteira de trabalho.')

else:
    numcarteira = int(input('Qual o número de sua carteira de trabalho? '))
    pessoa['carteira trabalho'] = numcarteira
    anotrabalho = int(input('Em que ano você começou a trabalhar c/ carteira? '))
    pessoa['Contratação'] = anotrabalho
    salario = float(input('Qual o seu salário hoje? R$ '))
    pessoa['salario'] = salario
    aposentadoria = (anotrabalho + 35) - aniver[2]
    pessoa['aposentadoria'] = aposentadoria


    print(f'\nO nome tem valor de {pessoa["nome"]}')
    print(f'A idade tem valor de {pessoa["idade"]} anos')
    print(f'CTPS tem valor de {pessoa["carteira trabalho"]}')
    print(f'Contratação tem valor de {pessoa["Contratação"]}')
    print(f'Salário tem o valor de R$ {pessoa["salario"]}')
    print(f'Aposentadoria tem valor de {pessoa["aposentadoria"]} anos')


print('\n Metodo 2\n')
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - date.today().year)
print('-=-' * 20)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')

print(dados)
