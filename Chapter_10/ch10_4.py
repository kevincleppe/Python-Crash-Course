filename= 'guests.txt'
ask="What would you like to write to the file: "
ask+="When you are done, enter 'q' "
active = True
guests=[]
with open(filename, 'w') as file_object:
    while active:
        guest=input(ask)
        guests.append(guest)
        file_object.write(f"\n{guest.title()}")
        if guest =='q':
            active = False
            break
        else:
            print("OK, we will add them to the list")
            

print(guests)

#rewrite this so q is not added ti list 