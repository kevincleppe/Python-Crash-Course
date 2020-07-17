alien_color=["green","red","yellow"]


for i in alien_color:
    if i == "green":
        print("5 points!")
    elif i =="red":
        print("15 points!")
    else:
        print("10 points!")
    
age =[1,2,3,5,19,32,2,22,12,32,55,6,14,2,55,88]

for i in age:
    if i ==1:
        print("You are a baby!!")
    elif i<=2:
        print("you are a toddler !")
    elif i<=3:
        print("you are 3!")
    elif i<=12:
        print("you are about to be a teenager!")
    elif i <=20:
        print("you are a teenager!")
    elif i <=65:
        print("You are an adult! Get a job!")
    else:
        print("You are so old!")

new_age=sorted(age)
print(new_age)
for i in new_age:
    if i ==1:
        print("You are a baby!!")
    elif i<=2:
        print("you are a toddler !")
    elif i<=3:
        print("you are 3!")
    elif i<=12:
        print("you are about to be a teenager!")
    elif i <=20:
        print("you are a teenager!")
    elif i <=65:
        print("You are an adult! Get a job!")
    else:
        print("You are so old!")