from random import randint

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

d6=Dice()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

d10 = Dice(sides=10)
results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

d11=Dice(sides=11)
tenresults=[]
for i in range (10):
    i=d10.roll_die()
    tenresults.append(i)
print("10 rolls of the 10 sided die: ")
print(f"\n{tenresults}")

d20=Dice(sides=20)
twentyresults=[]
for i in range (10):
    i=d20.roll_die()
    twentyresults.append(i)

print("Twenty sided results")
print(f"{twentyresults}")