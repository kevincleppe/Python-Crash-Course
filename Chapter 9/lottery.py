from random import choice

list =[1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e']
number=[]

while len(number) <5:
    i=choice(list)

    if i not in number:
        print(f"\nThe pulled number is a {i}")
        number.append(i)

print(number)