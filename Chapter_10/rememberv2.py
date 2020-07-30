import json
filename='usernamev2.json'

try:
    with open(filename) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("what is your name: ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We will remember you, {username}")

else:
    print(f"Welcome back {username}")