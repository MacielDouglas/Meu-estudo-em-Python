from pickle import TRUE


print('Programa tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até 20')
numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# opcao = int(input('Digite um número entre 0 e 20: '))
# while opcao > 20:
#     opcao = int(input('Tente Novamente. Digite um número entre 0 e 20: '))
# print(f'Vode digitou o número: {numero[opcao]}')

# print('Opçao melhor....')
while TRUE:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
   
        break
    print('Tente novamente..... ', end='')
print(f'Vode digitou o número: {numero[num]}')