print('pc escolhe um numero entre 0  e 10, e usurio vai tentar até acertar, mostrando no final quantos palpites')

from random import randint

computador = randint(1, 10)
print(computador)
user = None
palpite = 0
print('Vamos jogar. Veja se consegue acertar um numero de 0 a 10')
while user != computador:
    user = int(input('Digite um numero: '))
    palpite += 1

print('Acertou!!! O numero escolhido foi {}, e você acertou em {} palpites'.format(computador, palpite))


print('\nMétodo 2\n')
pc = randint(0, 10)
print('Sou seu pc... Escolhi um numério entre 0 e 10.')
print('Será que você consegue adivinhar???')
acertou = False
tentativas = 0


while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais uma vez...')
        elif jogador > pc:
            print('Menos... Mas não desista... ')
print('Acertou com {} tentarivas!!!'.format(tentativas))



