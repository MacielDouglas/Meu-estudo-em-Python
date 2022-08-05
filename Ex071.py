print('Simulação de Caixa Eletrônico')
print('====='*10)
print('-----'*3, end='')
print('   BANCO POUPE JÁ   ', end='')
print('-----'*3)
print('====='*10)

cinquenta = vinte = dez = um = 0
saque = int(input('Qual o valor que quer sacar? R$ '))
while True:
    while True:
        if saque >= 50:
            saque = saque - 50
            cinquenta += 1
        else:
            break
    while True:
        if saque >= 20:
            saque = saque - 20
            vinte += 1
        else:
            break
    while True:
        if saque >= 10:
            saque = saque - 10
            dez += 1
        else:
            break
    while True:
        if saque >= 1:
            saque = saque - 1
            um += 1
        else:
            break
    print(f'Total de {cinquenta} notas de R$ 50,00')
    print(f'Total de {vinte} notas de R$ 20,00')
    print(f'Total de {dez} notas de R$ 10,00')
    print(f'Total de {um} notas de R$ 1,00')
    break

print('Opção dois\n')
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte semrpe!!!')


