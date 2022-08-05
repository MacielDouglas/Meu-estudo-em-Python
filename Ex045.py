print('Jogo Jakenpô')
from random import randint
from time import sleep

computador = randint(0, 2)
jakenpo = ['papel', 'pedra', 'tesoura']

#print(computador)

print("Vamos jogar 'JAKENPÔ' escolha sua opção:\n"
      "0) Papel\n"
      "1) Pedra\n"
      "2) Tesoura\n")
usuario = int(input('Qual a sua escolha: '))

print('Processando....')
sleep(1)
if usuario == 0 or usuario == 1 or usuario == 2:
    usuario_escolha = jakenpo[usuario]
    computador_escolha = jakenpo[computador]
    if computador == 0 and usuario == 1 or computador == 1 and usuario == 2 or computador == 2 and usuario == 0:
        print('Voce perdeu!!! O computador escolheu: {}, e você: {}'.format(jakenpo[computador], jakenpo[usuario]))
    elif computador == 1 and usuario == 0 or computador == 0 and usuario == 2 or computador == 2 and usuario == 1:
        print('Parabens, voce ganhou!!! Você escolheu: {}, e o computador escolheu: {}'.format(jakenpo[usuario], jakenpo[computador]))
    else:
        print('Empate, ambos escolheram: {}' .format(computador_escolha))
else:
    print('Voce escolheu opção errada!!!')
