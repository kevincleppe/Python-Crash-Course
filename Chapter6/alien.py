alien_0 = {'color': 'green', 'points':5, 'position':"front"}

print(alien_0['color'])
print(alien_0['points'])
print(alien_0['position'])

new=alien_0['points']
print(f"You just earned {new} points!")

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)