import json
ask='Give me some numbers to add to the list: '
filename = '/Users/kev/Desktop/python/Python-Crash-Course/Chapter_10/text_files/numbers.json'
while True:
    add=input(ask)
    if add == 'q':
        break
    else:
        with open (filename, 'a') as f:
            json.dump(int(add), f)

