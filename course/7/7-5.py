charges = {'baby':'free','kid':'$10','teen':'$15'}

while True:
    age = int(input("How old are you?"))
    if age < 3:
        print(charges['baby'])
    elif age>=3 and age < 12:
        print(charges['kid'])
    elif age>=12:
        print(charges['teen'])
