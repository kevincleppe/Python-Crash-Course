filepath= '/Users/kev/Desktop/python/Python-Crash-Course/Chapter_10/text_files/million.txt'

with open(filepath) as file_object:
        contents = file_object.read()


pi_string=''
count=0
for content in contents:
    pi_string+=content
    count +=1

number=input("Give me a number ")
i=int(number)
print(f"{pi_string[i:52]}")
print(len(pi_string[:20]))
print(count)