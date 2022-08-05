print('Controle de velocidade, se passar de 80km será multado em R$ 7,00 por km acima da velocidade')

vel = int(input('Qual a velocidade do veículo: '))
mult = 7
tx = vel - 80
if vel > 80:
    print('Exessso de velocidade, você foi multado em R$ {:.2f}'.format(mult * tx))
else:
    print('Você é um motorista cuidadoso.')
print(tx)