filepath= '/Users/kev/Desktop/python/Python-Crash-Course/Chapter_10/numbers.txt'

with open(filepath) as file_object:
        contents = file_object.read()
        
    
for content in contents:
    print(content)