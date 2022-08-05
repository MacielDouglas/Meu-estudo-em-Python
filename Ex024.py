print('Leia um nome de uma cidade e diga se ela começa ou não com o nome Santo')

cidade = input('Digite o nome de uma cidade: ').strip()  
x = cidade.lower()
print("Existe a palavra 'SANTO' no nome desta cidade?", 'santo' in x[:5])
print(x[:5] == 'santo')