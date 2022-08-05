print('Calcular desconto')
preco = float(input('Qual o preço do produto: R$ '))
desconto = preco / 100 * 5
valor = preco - desconto
print('O produto custa R$ {}, e teve desconto de R$ {:.2f}, o valor a pagar é de R$ {:.2f}'.format(preco, desconto, valor))
