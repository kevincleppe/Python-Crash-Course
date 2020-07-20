
#Creates a variable with the assigned sentences attached to it
ask="How old are you?"
ask+="Enter in 'q' to quit out:"
#Creates a variable, 'active', that is equal to true
active=True
#while active is equal to true, do he following loop
while active:
    #Create an input
    age=(input(ask))
    #if the input is equal to 'q':
    if age.title() == 'Q':
        #Break from the loops
        active = False
        break
    #Converts the entered input from users to an integer
    #Compares the int to see how much the person's ticket will cost. 
    age=int(age)
    if age <= 3:
        print("The ticket is free!")
    elif age <=12:
        print("$11")
    elif age >= 13:
        print("$15")
    

print("You are here")

#Use this as a reference for that one code idea
