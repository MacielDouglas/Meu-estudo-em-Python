print('''Faça um programa que tenha uma função chamda escreva(), que receba um texto qualquer como parâmetro e 
Mostre uma mensgem com tamanho adaptável\n''')


def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)

escreva(str(input('Digite uma mensagem: ')))