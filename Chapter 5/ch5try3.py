current=["kevin","steve","kurtis","jack","jOhn"]
new=["john","kevin","jon","johhn","Jack"]
lower=[i.lower() for i in current]
print(lower)


for i in lower:
    if i in new:
        print(f"{i} is already taken! Pick another name")
    else:
        print(f"{i} is NOT taken! Congrats!")