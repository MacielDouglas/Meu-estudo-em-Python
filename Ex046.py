print('Contagem regressiva para fogo artificio 10 a zero pausa 1 segundo')

from time import sleep

for fogos in range(10, -1, -1 ):
    sleep(0.7)
    print(fogos)
print('Boom Baam Poow!!!')

