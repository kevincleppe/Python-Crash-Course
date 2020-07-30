import json

numbers = [1,2,3,4,5,6,7,22,1,23,123,123]

filename = '/Users/kev/Desktop/python/Python-Crash-Course/Chapter_10/text_files/numbers.json'
with open (filename, 'w') as f:
    json.dump(numbers, f)