print('Calculadora IMC')
altura = float(input('Digite a sua altura em cm: '))
peso = float(input(('Digite o seu peso em kg: ')))

imc = peso / (altura * altura) *10000
print(imc)
if round(imc, 2) <= 18.50:
    print('Voce esta abaixo do peso, seu IMC é de {:.2f}'.format(imc))
elif round(imc, 2) <= 25:
    print('Voce esta com peso ideal, seu IMC é de {:.2f}'.format(imc))
elif round(imc, 2) <= 30:
    print('Voce está com sobrepeso, seu IMC é de {:.2f}'.format(imc))
elif round(imc, 2) <= 40:
    print('Você está Obeso, seu IMC é de {:.2f}'.format(imc))
else:
    print('Voce está com Obesidade Mórbida, seu IMC é de {:.2f}'.format(imc))