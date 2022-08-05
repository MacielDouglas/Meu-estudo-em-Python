print('Calculo para ano bissexto')
import datetime
from datetime import date
ano = int(input('Digite um ano para calculo, ou zero para o ano atual: '))
# bissexto = ano % 4
# bissexto2 = ano % 100
if ano == 0:
    ano = date.today().year
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse é um ano Bissexto!!!')
    # if bissexto2 == 16:
    #     print('Esse ano é bissexto!')
    # else
else:
    print('Esse ano {} não é bissexto!'.format(ano))
