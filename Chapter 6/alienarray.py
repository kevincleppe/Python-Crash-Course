#Creates an empty array
aliens=[]

#creates a for loop that will loop 30 times
for i in range(30):
   #Creates a new array called new_alien with three key pairs
   #will append the info in this array to the previous array
    new_alien={'color': 'green', 'points': 5,'speed': 'slow'}
    aliens.append(new_alien)

#Will create a for loop that compare items in the aliens array
#If color matches with gree, will change the color to yellow, speed to medium, and points to 10
for i in aliens[:3]:
    if i['color']=='green':
        i['color']='yellow'
        i['speed']='medium'
        i['points']=10


#creates a for loop that will print the contents of alien array, butonly 5 times 
for i in aliens[:5]:
    print(i)
    #print(\n)
print("....")

print(f"total number of aliens: {len(aliens)}")