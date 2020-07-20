#Sets current to 0
current=0
#While current is less than 10, do these actions
while current <10:
    #Will add 1 to current
    current +=1
    #If current divided by two is equal to 0, aka even, 
    if current %2 ==0:
        #keep going 
        continue
    #Will print current, but only if an odd number
    print(current)