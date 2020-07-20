#Creates an empy dictionary called responses
responses={}

#creates a controlling variable set to True
polling=True

#While true do the following while loop
while polling:
    #Creates a user input called name, key for dictionary
    name= input("\nWhat is your name? ")
    #Creates a user input called name, value for dictionary
    response=input("Which mountain would you like to climb? ")

    responses[name]=response
    repeat =input("Would you like to let someone else respond? Enter no if no")
    if repeat=='no':
        polling = False

print("\n--Poll Results--")
for name, response in responses.items():
    print(f"{name} would like to climb {response}kev")

print(responses)