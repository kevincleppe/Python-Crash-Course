#Creates empty dictionary
places={}

#Creates variable equal to true
ask = True

#While true 
while ask:
    #User prompt
    name= input("What is your name? ")
    #User prompt
    place=input("What place would you like to visit in the world? ")
    #Associates input to dictionary
    places[name]=place

    again=input("Does anyone else want to answer? ")
    if again == 'no':
        ask = False
print(places)