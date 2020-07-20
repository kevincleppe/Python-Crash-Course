#Prints a statements 
prompt="\nTell me something and I will repeat it"
#Gives an additional statement
prompt+="\nEnter 'quit' to end the program: "
words=[]
#Sets a flag, 'active', that is equal to true
active = True
#While active is equal to true, go through the below loop
while active:
    #Gives users a prompt to input a message
    message = input(prompt)
    words.append(message)
    #If the input is equal to to 'quit', set active flag to False, which then quits out 
    if message.title()  == 'Quit':
        words.remove(message)
        active= False
        break
    else:
        print(message)

print("You have exited the loop")
print(words)