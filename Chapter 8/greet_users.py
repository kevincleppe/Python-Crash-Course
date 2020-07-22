def greet(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
    
usernames = ['kev','kevin','kerv']
greet(usernames)