set1 = {'CArlos', 'pedro', 'Silvia', 'mateus', 'josé'}
set2 = {'Pedro', 'pedro', 'Silvia', 'silvania', 'milena'}

set1.union(set2)
print(set1.union(set2))
print(set2.difference(set1))
print('dicionario')
dic11 = {
    'Nome': 'Douglas',
    'Idade': 40,
    'Cidade': 'Olindda',
    'Profissão': 'Programador'
}
print(dic11['Nome'])
print(type(dic11))

armarinho = {
    'Nome': 'Douglas',
    'Idade': 40,
    'Cidade': 'Olindda',
    'Profissão': 'Programador'
}
print(armarinho, type(armarinho))

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print('Before reshaping:')
print(arr)
print('\n')

arr1 = arr.reshape(2, 2, -1)
print('After reshaping:')
print(arr1)
print('\n')


data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100


plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()


import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]
slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')

plt.title('Pie Plot')
plt.show()

