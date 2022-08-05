print('Leia o ano de nascimento de um jovem e informa se ele vai se alistar ou se já pasou a data.')

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Qem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual +saldo
    print('Voce ainda não tem 18 anos. Ainda falta {} anos para o alistamento, que ocorrerá em {}'.format(saldo, ano))
elif idade > 18:
    saldo = idade - 18
    anos = atual - saldo
    print('Você já passou a idade de alistar, e deveria ter alistado há {} anos. O ano do seu alistamento foi em {}'.format(saldo, anos))





