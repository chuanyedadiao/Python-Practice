places = {}

active = True

while active:
    print("\nThanks for taking part in this investigation.")
    username = input("Enter your name:")

    place = input("\nIf you could vidit ont places in the world, where would you go?")

    places[username] = place

    infor = input("continue investigate?(yes/no)")

    active = True if infor == "yes" else False 
