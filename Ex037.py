print('Escreva um programan que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversao: binario, otcal, hexadecimal')

num = int(input('Digite um numero inteiro qualquer: '))
binar = bin(num)
oct = oct(num)
hexa = hex(num)

# print('bin: ', binar, ' otca: ', oct, ' hexad: ', hexa)

opc = int(input('Escolha uma opção para conversão: \n1) para binário;\n2) para Octal;\n3)para hexadecimal\nQual a sua opção: '))

if opc == 1:
    print('O numero {}, convertido em Binário é: {}'.format(num, binar[2:]))
elif opc == 2:
    print('O numero {} convertido para Octal, é: {}'.format(num, oct[2:]))
elif opc == 3:
    print('O numero {}, convertio para Hexadecimal é: {}'.format(num, hexa[2:]))
else:
    print('Voce escolheu uma opção inválida!!!')


