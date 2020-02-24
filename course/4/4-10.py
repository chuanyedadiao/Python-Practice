foods = ['pizza','falafel','carrot cake','cannoli','ice cream']

print('The first three items in the list are:')

for food in foods[:3]:
    print(food)

print('\n\nthree items in the middle of the list are:')

for food in foods[1:4]:
    print(food)

print('\n\nThe last three items in the list are:')

for food in foods[-3:]:
    print(food)
