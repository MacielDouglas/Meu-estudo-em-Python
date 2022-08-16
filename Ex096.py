print('Prog. c/ funçao chamada area(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a area do terreno\n')
def area(a, b):
    s = a * b
    print(f'A area de um terreno {a} x {b} é de {s:.1f}m²')

print('Controle de Terrenos')
print('-' * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)

