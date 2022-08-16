def leiaInt(str):
    while True:
        x = input(str)
        if x.isnumeric() == True:
            numero = int(x)
            break
        else:
            print('\033[0;31mERRO!!! Digite um número válido!!!\033[m')
    return numero


n = leiaInt('Digite um numero: ')
print(f'Você digitou o numero {n}')


