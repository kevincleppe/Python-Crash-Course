from die import Die

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#print(results)

frequencies =[]
for value in range(1, die.num_sides+1):
    freq=results.count(value)
    frequencies.append(freq)
    print(f"{value} {freq}")

print(frequencies)