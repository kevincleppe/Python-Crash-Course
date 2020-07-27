filename = 'learned.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    print("Style 1")
    for line in lines:
        print(line)

with open(filename) as f:
    contents =f.read()
    print("Style 2")
    print(contents)