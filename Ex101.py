print('''Programa com funçao voto(), recebe como parametro o ano de nasciemtno de uma pessoa.
Retrona um valor literal indicando se uma pessoa tem voto, NEGADO, OPCIONAL OU OBRIGADTÓRIO.\n''')


def voto(num):
    from datetime import date
    hoje = date.today().year
    idade = hoje - num
    if idade < 16:
        print(f'Você tem: {idade} anos, e ainda não vota.')
    elif idade >= 18 and idade <= 64:
        print(f'Você tem {idade} anos, o seu voto é obrigatório')
    else:
        print(f'Você tem {idade} anos, e seu voto é opcional.')


voto(int(input('Em que ano você nasceu? ')))

