import json

filename = '/Users/kev/Desktop/python/Python-Crash-Course/Chapter_10/text_files/numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)