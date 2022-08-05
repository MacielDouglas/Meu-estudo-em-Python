print('PC escolhe um numero e o usuario tenta adivinhaar')
from random import randint
from time import sleep

# import random
# x = [0, 1, 2, 3, 4, 5]
# num = int(random.choice(x))
num = randint(0, 5)
y = int(input('Digite um numero entre 0 e 5: '))
print('Analizando.......')
sleep(2)
if y == num:
    print('\nVoce acertou!!\n' * 3)
else:
    print('\nKkkkk, você errou!!!\n')
print('O computador escolheu {}, e você escolheu {}'.format(num, y))