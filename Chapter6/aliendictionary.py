#this creates a dictionary called alien 0, with three key pairs
alien_0={'x_position':0, 'y_position': 25, 'speed':'fast','points':'5'}
#This prints the initial position of the alien 
print(f"Original position: {alien_0['x_position']}")
#this creates a series of if else statements that will determine how much to inrement the x position by
if alien_0['speed'] =='slow':
    x_increment = 1
elif alien_0['speed']== 'medium':
    x_increment = 2
else:
    x_increment = 3
#this will use the int from the above if else statements to determine how much to increment the x position by
alien_0['x_position'] = alien_0['x_position'] + x_increment
#this will print the new position that was determined by the if then statments 
print(f"New position: {alien_0['x_position']}")

print(alien_0)
del alien_0['points']
print(alien_0)