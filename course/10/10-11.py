import json

def read_in():
    number = input("Please enter you favorite number:")
    try:
        with open("number.txt","w") as num:
            json.dump(number,num)
    except FileNotFoundError:
        print("number.txt is not found")

def read_out():
    try:
        with open("number.txt") as num:
            number = json.load(num)
            print("I know your favorite number!It's "+ number)
    except FileNotFoundError:
        print("number.txt is not found")
    

read_in()

read_out()
