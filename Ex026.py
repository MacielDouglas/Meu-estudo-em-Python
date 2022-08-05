from itertools import count


print('Programa que leia uma frase e mostre,\nQuantas vezes aparece a letra: A\nEm que posição aparece a primeira letra\nEm que posição aparece a ultima')

desafio = input('Digite uma frase qualquer: ').strip()
x = desafio.lower()
print("A letra 'A', aparece: {} vezes nesta frase" .format(x.count('a')))
print('A primira posição que aparece a letra A é {}' .format(x.find('a')))
print('A ultima posição que aparece a letra A é {}' .format(x.rfind('a'))) #Procura a apartir da ultima letra