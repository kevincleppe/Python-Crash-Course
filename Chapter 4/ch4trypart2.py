numbers=[1,2,3,4,5,6,7]
print(numbers)
print(numbers[:3])
print(numbers[2:5])
print(numbers[4:])

pizza=['sausage','pepperoni', 'cheese', 'olive']
friend_pizza=pizza[:]
friend_pizza.append('test')
for i in pizza:
    print (i)
    print("I like", (i.title()), "pizza")
    print(pizza)
    print(friend_pizza)

print("I really love pizza!")