unprinted=['case', 'robot', 'triangle']
completed=[]

while unprinted:
    current=unprinted.pop()
    print(f"Now printing {current}")
    completed.append(current)


for i in completed:
    print(f"Now done with {i}")
print("you are here")