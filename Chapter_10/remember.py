import json
user=input("What is your name: ")

filename='username.json'
with open(filename, 'w') as f:
    json.dump(user, f)
    print(f"{user}")