print('Programa calcula valor a pagar mediante metodo pagamento')

valor_produto = float(input('Digite o valor do produto a ser pago R$: '))
formaPgto = int(input("Escolha a fomar de pagamento:\n"
                "1) A vista dinheiro 10% desconto;\n"
                "2) `A vista cartão: 5% desconto;\n"
                "3) Em ate 2x no cartão, preço normal;\n"
                "4) 3x no cartão, juros 20%;\n"
                      "Qual a forma de pagamento: "))

if formaPgto == 1:
    print('Você recebeu 10% desconto, o valor a pagar é: R$ ', valor_produto - ((valor_produto / 100) * 10))
elif formaPgto == 2:
    print('Voce recebeu 5% desconto, o Valor a pagar é: R$ ', valor_produto - ((valor_produto / 100) * 5))
elif formaPgto == 3:
    print('O Valor a pagar é R$ {:.2f}' .format(valor_produto))
elif formaPgto == 4:
    print('Voce recebeu parcelamento em 3x, o valor a pagar é: ', valor_produto + (valor_produto / 100 * 20))
else:
    print('Forma de pagamento inesistente')


