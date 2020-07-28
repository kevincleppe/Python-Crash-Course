#Program will ask user for two sets of prompts
#First, a list of cats


try:
    catfile='/Users/kev/Desktop/python/Python-Crash-Course/cats.txt'
    cat_ask="Name some cats: "      
    with open(catfile, 'w') as file_object:
        while True:
            cat=input(cat_ask)
            if cat == 'q':
                break
            else:
                cat_contents=file_object.write(f"\n{cat.title()}")
                print("Ok, adding to the list: ")
                print(f"--{cat.title()}")
except FileNotFoundError:
    print("hmmmm")

try:
    with open(catfile) as file_object:
        lines = file_object.readlines()
        for line in lines:
            print(line)
except FileNotFoundError:
    print("Hey")

dogfile='/Users/kev/Desktop/python/Python-Crash-Course/dogs.txt'
dog_ask="Name some dogs: "
with open(dogfile, 'w') as file_obj:
    while True:
        dog=input(dog_ask)
        if dog == 'q':
            break
        else:
            dog_contents=file_obj.write(f"\n{dog.title()}")
            print("Adding dog to file")
            print(f"--{dog.title()}")

with open(dogfile) as file_obj:
    lines=file_obj.readlines()
    for line in lines:
        print(line)