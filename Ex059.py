print('Leia dois valores e mostre um menu de opções: ')

num1 = int(input('Digite o primeiro numero inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
result = 0
operacao = 0
while operacao != 5:
    result = 0
    operacao = int(input('Escolha uma opção:\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair\nQual a sua opção: '))
    if operacao == 1:
        result = num1 + num2
        print(result)
        break
    if operacao == 2:
        result = num1 * num2
        print('A multiplicação dos valores é:', result)
        break
    if operacao == 3:
        if num1 > num2:
            result = num1
            print('O maior numero foi {}'.format(result))
            break
        else:
            result = num2
            print('O maior numero foi {}'.format(result))
            break


    if operacao == 4:
        num1 = int(input('Digite novamente o primeiro numero inteiro: '))
        num2 = int(input('Digite novamente o segundo número inteiro: '))

print(result)

print('Fim do programa!')

print('\nMetodo 2\n')
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do progrma''')
    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))

    elif opcao == 2:
      produto = n1 * n2
      print('O resultado de {} x {} é {}'.format(n1, n2, produto))

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))

    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando....')

    else:
        print('Opção inválida. Tente novamente')
    print('x-x' *10)
    sleep(2)
print('Fim do programa! Volte sempre')