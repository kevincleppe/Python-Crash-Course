filepath= '/Users/kev/Desktop/python/Python-Crash-Course/Chapter_10/text_files/numbers.txt'

with open(filepath) as file_object:
        contents = file_object.read()

pi_string=''
count=0
for content in contents:
    pi_string+=content
    count +=1
birthday=input("Enter your birthday, in the form of mmddyy: ")
if birthday in pi_string:
    print(f"Your birth of {birthday} is in pi!")
else:
    print("Your birthday is not in pi.")
birthint=int(birthday)
active=True
x=0
while active:
    i=pi_string[x:x+4]
    if i !=birthint:
        i=pi_string[x:x+4] 
        print(i)
        x+=1
    else:
        print("test")
        active=False
        break

    
print(f"{pi_string[:x]}")
