print('Conversor de metros para centimentos e milimetros')

metros = float(input('Digite um valor em metros: '))
centimentros = metros * 100
milimetros = centimentros * 100

print('O valor em metros foi {}\nEsse valor em centímetros é {:.0f}\nE em milímetros é {:.0f}'.format(metros, centimentros, milimetros))
