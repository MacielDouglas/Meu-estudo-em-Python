print('Melhorar o desafio anterior perguntando se o usuario quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos')

primeiro = int(input('Insiro o primeiro o termo: '))
razao = int(input('Raza da PA: '))
termo = primeiro
cont = 1
contado = 10
newcont = 1

while newcont != 0:
    while cont <= contado:
        print(' {} -->'.format(termo), end='')
        termo += razao
        cont += 1
    print(' PAUSA')
    newcont = int(input('Quantos termos você quer mostrar a mais? '))
    contado += newcont

print('FIM!!!')



