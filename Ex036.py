print('Emprestimo, qual o valor da casa, o salario e em quantos anos.\nCalcule o valor da prestação mensal sabendo que ela não pode esceder 30% do salário.')

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salario? '))
anos = float(input('Em quantos anos irá finaciar a casa? '))

meses = anos * 12
parcelas = casa / meses
posso = (salario / 100) * 30
print('Parcelas valor: {:.2f}'.format(parcelas))
print('30% do salario:', posso)
if posso >= parcelas:
    print('Você pode financiar a casa. A parcela é de R$ {:.2f}. O finacimaneto será em {:.0f} meses.'.format(parcelas, meses ))
else:
    print('Infelizmente você não pode financiar a casa, a parcela de {:.2f} ultrapassa os 30% do seu salario.'.format(parcelas))


(print('Opção 2: '))
prestacao = casa / (anos * 12)
mínimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= mínimo:
    print('Empr´stimo pode ser concedido')
else:
    print('Emprestimo negado')

