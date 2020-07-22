def person(first,last, age=None):
    person ={'first': first, 'last': last}
    if age:
        person['age']=age
    return person

test=person('kevin','cleppe', 30)
print(test)