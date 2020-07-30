import json

def get_rememebered_name():
    filename='usernamev2.json'
    try:
        with open(filename) as f:
            usernamev2= json.load(f)
    except FileNotFoundError:
        return None
    else:
        return usernamev2

def greet_user():
    username = get_rememebered_name()
    if username:
        print(f"Welcome back {username}")
    else:
        username=input("What is your name: ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back {username}")

greet_user()