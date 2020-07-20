#Creates a filled array
unconfirmed=['kevin','devin', 'evan','levin','cevin']
#Creates an empy array
confirmed=[]
#Creates a while loop that will loop as long as there are elements in the unconfirmed array
while unconfirmed:
    #Will pop an element from unconfirmed, and attach it to the current variable
    current =unconfirmed.pop()
    #Will print a statement that contains the current variable.
    print(f"Verifying user: {current.title()} ")
    #Will append the current element to the confirmed array
    confirmed.append(current)

#When the loop finishes, will come here
print("\nThe following users have been confirmed: ")
for i in confirmed:
    print(i.title())

#Variation idea:
#This, but instead of a predetermined array, allow users to add in their own variables 
#Oh I've already done this..
