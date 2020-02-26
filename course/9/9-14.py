from random import randint

class Die():
    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        x = randint(1,self.sides)
        print(x)


die1 = Die()
print("\n6 sides:")
for _ in range(10):
    die1.roll_die()
    
die2 = Die(10)
print("\n10 sides:")
for _ in range(10):
    die2.roll_die()

die3 = Die(20)
print("\n20 sides:")
for _ in range(10):
    die3.roll_die()
