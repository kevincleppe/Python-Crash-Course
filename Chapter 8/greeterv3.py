def formatted(first, last):
    full=f"{first} {last}"
    return full.title()

while True:
    print("\nPlease tell me your name: ")
    first_name=input("First name: ")
    if first_name =='q':
        break
    last_name=input("Last name: ")
    if last_name =='q':
        break
    formatted=(first_name,last_name)
    print(formatted)