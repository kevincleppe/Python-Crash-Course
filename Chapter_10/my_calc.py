
while True:
    first=input('First number: ')
    if first =='q':
        break
    second=input("Second number: ")
    if second =='q':
        break
    try:
        answer= float(first) / float(second)
    except ZeroDivisionError:
        print("You cannot dvide by zero")
    except ValueError:
        print("Make sure to only input numbers")
    else:
        print(answer)