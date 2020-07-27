filename = '/Users/kev/Desktop/python/Python-Crash-Course/Chapter_10/pets.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    print("Style 1")
    for line in lines:
        print(line.replace('cats','dogs'))