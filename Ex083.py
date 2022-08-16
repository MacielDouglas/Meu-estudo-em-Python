print('O usuario digite uma expressão matemática e o programa avalia se a expressão está correta, com os parênteses abertos e fechados na ordem correta\n')

expressao = str(input('Digite aqui a sua expressão: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está errada!')


