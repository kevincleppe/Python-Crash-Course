nums=['1','222','42','11','74', '123','153','69']
real_nums=[]
print(nums)
print(real_nums)
for i in range(len(nums)):
    t = int(nums[i])
    real_nums.append(t)
    print(real_nums)

    print("this will hopefully print out the list in numerical order")

for i in real_nums:
    real_nums.sort()
    print([i])

for i in (real_nums):
    if len(real_nums) > 0:
        if i < 55:
            print([i], " is lower than 55")
        elif i == 69:
            print([i],"? nice")
        elif i >55:
            print([i], "Is higher than 55")
        
        