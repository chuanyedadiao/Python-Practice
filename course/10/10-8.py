try:
    with open("cats.txt") as cat:
        print(cat.read())
except FileNotFoundError:
    pass
try:
    with open("dogs.txt") as dog:
        print(dog.read())
except FileNotFoundError:
    pass
