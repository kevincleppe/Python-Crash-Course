number=(input("enter a number, and ill tell you if its even or odd, or type q to quit"))

while number !='q':
    number=int(number)
    if number %2 ==0:
        print(f"{number} is even")
        break
    else:
        print("Number is odd")
        break

if number == 'q':
    print("Quitting out")

