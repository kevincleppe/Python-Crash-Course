def formatted(first,last, middle=''):
    if middle:
        full=f"{first} {middle} {last}"
    else:
        full=f"{first} {last}"
    return full.title()

me=formatted('kevin','the', 'cleppe')
you=formatted('test','user')
print(me)
print(you)