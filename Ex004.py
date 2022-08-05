#Dissecando uma variavel
print('Exercício, dissecando uma variável:')

x = input('Digite algo: ')
print('O tipo primitivo disso é: ', type(x))
print('É um alfabético:', x.isalpha())
print('É um alfanumérico:', x.isalnum())
print('Está em minúsculo:', x.islower())
print('Está tudo maiuscúlo:', x.isupper())
print('Só tem espaço:', x.isspace())
print('É um número:', x.isnumeric())
print('Está capitalizada: ', x.istitle())


