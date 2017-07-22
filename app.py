# Describe the schetch comedy group

name = 'Montey Python'
description = 'sketch comedy group'
year = 1969

# best works

famous_sketch = "\n\tGood's"
famous_sketch1 = "\n\tMontey's adventure"

print('Best works: ' + famous_sketch1 + famous_sketch)

# Introduce them
sentence = name + ' is a ' + description + ' formed in ' + str(year)
print(sentence)

day = input('Che giorno è, pizda mati?')

print('hai scritto: ', day)


# lists

list = []
list.append('piselle')
list.append('cornuti froci')

print(list)


# dictionaries
dizionario = {}

dizionario['pizda mati'] = 'figa di tua mamma'

print(dizionario['pizda mati'])

import random

for i in range(10):
    ticket = random.randint(1, 1000)
    print(ticket)


# Dizionario della mia piadineria

menu = {'Menu_1:' : ['Piadina', 'Bibita a scelta', 'Dolce a scelta'],
        'Menu_2:' : ['Pizza', 'Bibita a scelta', 'Dolce a scelta' ],
        'Menu_3:' : ['Patatine', 'Bibita a scelta', 'Dolce a scelta']}

print(menu['Menu_3'])
