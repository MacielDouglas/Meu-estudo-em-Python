print('Exercicio 15, Alguel de carros')

dias = int(input('Por quantos dias você alugou o carro: '))
km = float(input('Quantos kilometros você rodou como carro: '))
total = (dias * 60) + (km * 0.15)

print('O valor total a pagar é de R$ {:.2f}'.format(total))
