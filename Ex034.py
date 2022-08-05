print('Calcule aumento salario, pra superior a R$ 1.250,00 aumento 10%, e inferior aumento 15%')

salario = float(input('Qual o seu salário: '))
# nv_salario = float
if salario >= 1250.00:
    nv_salario = salario / 100 * 10 + salario
else:
    nv_salario = salario / 100 * 15 + salario

print('O seu novo salario é e R$ {:.2f}'.format(nv_salario))
