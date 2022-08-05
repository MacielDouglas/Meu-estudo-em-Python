print('Contador para saber quais pessoas já atingiram maior idade.')

from datetime import date # importar o ano atual
atual = date.today().year # para pegar o ano da máquina
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menors de idade'.format(totmenor))

