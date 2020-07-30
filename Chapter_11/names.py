
from name_funtion import get_formatted_name

print("Enter 'q' anytime to quit")

while True:
    first=input("Give me a first name: ")
    if first == 'q':
        break
    last = input ("Give me a last name: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)

    print(f"\n\tNeatly formatted: {formatted_name}")