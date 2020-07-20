def describe_pet(type, name='steve'):
    print(f"\nI have a {type}")
    print(f"\nMy {type}'s name is {name.title()}.'")

describe_pet('hamster','harry')
describe_pet('dog', 'robin')
describe_pet(name='steve',type='monkey')
describe_pet(type='dog')