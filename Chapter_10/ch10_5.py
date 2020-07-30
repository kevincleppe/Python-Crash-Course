filename= '10_.5txt'
ask="What have you learned about programming: "
ask+="When you are done, enter 'q' "
active= True
with open(filename, 'a') as file_object:
    while active:
        learned=input(ask)
        file_object.write(f"\n{learned.title()}")
        if learned.title() == 'Q':
            active = False
            break
        else:
            print("Ok, we will add it to the list")

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line)