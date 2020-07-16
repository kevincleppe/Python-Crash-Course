for value in range (1,20):
    print (value)

numbers = list(range(1,100))
print(sum(numbers))
print(min(numbers))
print(max(numbers))


for i in range(1,100,3):
    if i % 2!= 0:
        print (i)
print("this will print divisables of 3 between 1 and 30")
for x in range (1,30):
    if x%3 == 0:
        print(x)

print("Testing cubes")
for z in range (1,10):
    print(z**3)