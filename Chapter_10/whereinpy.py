#This script will tell you if your Bday is in Pi
#Will also print out how far into Pi your Bday is

#This is the file we are using as Pi reference
filepath= '/Users/kev/Desktop/python/Python-Crash-Course/Chapter_10/text_files/million.txt'

#This will read the contents from the above file
with open(filepath) as file_object:
        contents = file_object.read()
#Empty string
pi_string=''
#Will add charcters from the file to the empty string 
for content in contents:
    pi_string+=content

birthday=input("Enter your birthday, in the form of mmddyy: ")
if birthday in pi_string:
    print(f"Your birth of {birthday} is in pi!")
else:
    print("Your birthday is not in pi.")
x=0
active = True
z= 4
while active:
    i=pi_string[x:x+z]
    a=pi_string[0:x+z]
    if i ==birthday:
        print(pi_string[0:x+z])
        active = False
        break
    else:
        x+=1





