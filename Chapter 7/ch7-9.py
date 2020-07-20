sand=['blt','turkey','chicken','past','past','past']

while 'past' in sand:
    sand.remove('past')
fin=[]

while sand:
    current=sand.pop()
    print(f"making {current} now")
    fin.append(current)

print(fin)


#Add in code that will account for only a certain amout of maerials per sandwhich left
#Will print avaiable sandwiches left 