from ch9_6 import IceCreamStand, Restaurant


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry','rocky road']
big_one.describe_restaurant()
big_one.show_flavors()
big_one.total_flavors()

channel_club = Restaurant('the channel club', 'steak and seafood')
channel_club.describe_restaurant()


bask=IceCreamStand("Baskin Robins")
bask.flavors=['Lemon','apple','oranges']
bask.describe_restaurant()