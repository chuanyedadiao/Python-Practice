pizzas = ['chicken pizza','beef pizza','pork pizza']

friend_pizzas = pizzas[:]

pizzas.append('fruit pizza')

friend_pizzas.append('cola pizza')

print('My favorite pizzas are: ')

for pizza in pizzas:
    print(pizza)

print('My friend\'s favorite pizzas are:')

for pizza in friend_pizzas:
    print(pizza)
