print('''Prog, função fatorial() que recebe dois parametros: o primeiro que indiqua o número a calcular eo o outro chamado show.
O show é um valor lógico(opcional) indicando se será mostrado ou nao na tela o processo de cálculo do fatorial.\n''')


def fatorial(num=1, show=False):
    '''
    => Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :pram show: (opcional) Mostrar ou não a conta.
    :return: O Valor do Fatorial de um número n.
    '''
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            print(f'{c} x 'if c > 1 else f'{c} = ', end='')
    return f


#x = fatorial(2, False)
num = int(input('Digite um numero: '))
show = bool(input('Quer ver as multiplicaçoes? [enter para não ou qualquer carecter para sim}: '))
print(fatorial(num, show))


# Opçao dois


def fatorial2(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial2(5, show=True))
