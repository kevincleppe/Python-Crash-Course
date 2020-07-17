#creates a dictionary with three key pairs 
user_0= {
    'username': 'efermi',
    'first': 'enrico',
    'last':'fermi',
}
#creates a for loop that loops through the items in the dict, one print for the key, and then one for the value
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"value: {value}")
#This for loops will loop through the items in he dictionary specified above, and will print the leys
for key in user_0.keys():
    print(key.title())