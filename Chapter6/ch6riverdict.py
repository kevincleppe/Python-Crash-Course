rivers={
    'eygpt':'nile',
    'brazil': 'amazon',
    'russa':'russian river',
}

for key,value in rivers.items():
    print(f"there is a river in {key} called the {value} river")

for i in rivers.keys():
    print(i)

for x in rivers.values():
    print(x)