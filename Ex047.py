print('Mostrar todos os numeros pares de 1 e 50')

for x in range(1, 51):
    if x % 2 == 0:
        print(x)

print('Para fazer a metade das repetiçoes: ')
# Dessa forma o laço for fará metade das repetições.
for n in range(2, 51, 2):
    print(n)
print('Fim')