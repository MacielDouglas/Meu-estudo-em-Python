print('Verificar se uma frase é um palíndromo')

frase = str(input('Digite uma frase para saber se é um palíndromo: ')).strip().lower()
frase = ''.join(frase.split())
print('O inverso de {} é {}'.format(frase, frase[::-1]))
if frase == frase[::-1]:
    print('Sim é um palindromo')
else:
    print('Não é um palindromo!!')




print('metodo 2')

frase2 = str(input('Digite uma frase, para metodo 2: ')).strip().upper()
palavras = frase2.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(frase2, inverso))
if inverso == junto:
    print('TEmos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')