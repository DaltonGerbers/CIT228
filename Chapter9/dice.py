from random import randint
class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

d6 = Die(6)
print("Rolling D6:")
for x in range(10):
    d6.roll_die()

d10 = Die(10)
print("Rolling D10:")
for x in range(10):
    d10.roll_die()

d20 = Die(20)
print("Rolling D20:")
for x in range(10):
    d20.roll_die()