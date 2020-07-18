#this creates a dictionary of me with three key pairs
kevin={'height':6, 'age':30, 'location': 'redlands'}
charo={'height': 5, 'age':40, 'location': 'highland'}
asun={'height': 5.5, 'age':55, 'location': 'yucaipa'}
#this associates with the different key pairs to specific variables 
tall=kevin['height']
old=kevin['age']
place=kevin['location'].title()

peeps=[kevin, charo, asun]

for i in peeps:
    print(i)
#this prints out those variables from above 
#print(tall)
#print(old)
#print(place)

#nums={'kevin':22, 'johnny':43, 'sarah':55}


#num1=nums['kevin']
#print(num1)