print('Leia um angulo qualquer e mostre na tela: \nO valor do seno.\ncosseno\ntangente desse angulo')

import math
angulo = float(input('Digite o angulo que deseja: '))
seno = math.sin(math.radians(angulo))
print('L angulo de {} tem o seno de {:.2f}'.format(angulo, seno))

cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))

tangente = math.tan((math.radians(angulo)))
print('A tangente de {} é de valor {:.2f}'.format(angulo, tangente))


