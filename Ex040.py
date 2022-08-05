print('Media de notas de um aluno')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
md = (n1 + n2) / 2

if md >= 7:
     print('Aprovado!!!  A média foi de {}'.format(md))
elif md >= 5:
    print('Esta em recuperação, a média foi de: {}'.format(md))
else:
    print('Reprovado, a média foi {}'.format(md))