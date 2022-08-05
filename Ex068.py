print('Jogo par ou impar, jogo é interrompido quando usuario perder\n')

print('VAMOS JOGAR PAR OU IMPAR!!!')

from random import randint

cont = 0
while True:
    num1 = int(input('Escolha um número: '))
    user = str(input('Você quer par ou impar [P/I]? ')).lower().strip()[0]
    print('---' * 20)
    comp = randint(1, 10)
    x = num1 + comp



    if x % 2 == 0:
        result = 'par'
    else:
        result = 'impar'

    print(f'Você jogou {num1} e o computador {comp}. Resultado: {x}, é {result}')

    if user == result[0]:
        cont += 1
        print('Voce Ganhou!!!')

    else:
        print('Voce Perdeu!!!')
        print('=-'*30)
        print(f'GAME OVER!!! Você venceu {cont} vezes')
        break


print('\nOpção dois\n')
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce Venceu!')
            v += 1
        else:
            print('Voce Perdeu!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce Venceu!!!!!')
            v += 1
        else:
            print('Voce Perdeu!!!!!')
            break
    print('Vamos Jogar Novamente????')
print(f'GAME OVER!!!\nVoce venceu {v} vezes.')
