print('Categoria pelo ano de nascimento')
'''from datetime import datetime

# solicita o ano de nascimento do usuario, e já converte para data, ano
nasc = datetime.strptime(input('Em que ano nascimento: '), '%Y').year
# pega o ano atual do pc
data = datetime.today().year
idade = data - nasc
'''
## outra opcao
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nacimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('A sua categoria é: MIRIM, pois sua idade é {} anos'.format(idade))
elif idade <= 14:
    print('A sua categoria é: INFATIL, pois a sua idade é: {} anos'.format(idade))
elif idade <= 19:
    print('A sua categoria é: JUNIOR, pois a sua idade é: {} anos'.format(idade))
elif idade <= 25:
    print('A sua categoria é:SENIOR, pois a sua idade {} anos'.format(idade))
else:
    print('A sua categoria é: MASTER, pois a sua idade é: {} anos'.format(idade))



