print("""Digite sete valores numericos e cadastre em uma lista única, separada de pares e impares.
No final mostre os valores pares e impares em ordem crescente.\n""")

numericos = [[], []]
for x in range(1, 8):
    numero = int(input(f'Digite o {x}º valor: '))
    if numero % 2 == 0:
        numericos[0].append(numero)
    else:
        numericos[1].append(numero)

print(f'Os números digitados pares são: {sorted(numericos[0])}')
print(f'Os numeros digitados impares são: {sorted(numericos[1])}')



