print('Prog. pergunta a distancia de uma viagem em KM. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longa')

km = float(input('Qual a distancia da viagem? '))
preco = float()
if km <= 200:
    preco = 0.5
else:
    preco = 0.45

print('O valor a pagar na passagem é de R$ {:.2f}'.format(km * preco))

preço_passage = km *0.50 if km <= 200 else km * 0.45
print(preço_passage)

