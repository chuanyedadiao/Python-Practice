import json

try:
    with open("number.txt") as num:
        number = json.load(num)
except FileNotFoundError:
    number = input("Please enter you favorite number:")
    with open("number.txt","w") as num:
        json.dump(number,num)
else:
    print("I know your favorite number!It's "+ number)
