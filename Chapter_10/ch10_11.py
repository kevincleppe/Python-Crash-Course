import json
filename= 'favorite_number.json'

try:
    with open(filename) as f:
        favorite_number=json.load(f)
except FileNotFoundError:
    fav_num=input("what is your favorite number: ")
    with open(filename, 'w')as f:
        json.dump(fav_num, f)
        print(f"Your favorite number is {fav_num}")

with open(filename) as f:
    numbers = json.load(f)

print(numbers)
print(f"Number pulled from file {numbers}")