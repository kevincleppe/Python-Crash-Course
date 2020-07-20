ask="What would you like on your pizza? "
ask+="When you are done, enter q: "
active = True
toppings=[]
while active:
    top=input(ask)
    toppings.append(top)
    if top.title()=='Q':
        active= False
        break
    else:
        print(f"Ok, we will add {top} to your pizza")

print(f"You have requested {toppings} on your pizza.")
print("exiting loop")