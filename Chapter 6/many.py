users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location': 'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location': 'paris',
    },
}

for username,info in users.items():
    print(f"\nusername: {username}")
    full=f"{info['first']} {info['last']}"
    location=f"{info['location']}"
    print(f"\tFull name: {full.title()}")
    print(f"\tLocation: {location.title()}")