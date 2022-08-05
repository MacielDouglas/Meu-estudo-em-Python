print('Programa aumento de salário 15%')

salario = float(input('Digite qual é o salário atual R$ '))
aumento = salario / 100 * 15
novo_salario = salario + aumento
print('O novo salario será com o aumento de 15% de R$ {:.2f}'.format(novo_salario))

nvsalaria = salario + (salario * 15 / 100)
print('O resultado é o mesmo R$ {:.2f}'.format(nvsalaria))