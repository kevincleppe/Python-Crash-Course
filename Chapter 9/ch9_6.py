class Restaurant:
    def __init__(self, food_type,describe):
        self.type= food_type
        self.describe=describe

    def describe_restaurant(self):
        print(f"The restaurant is {self.describe} and our best meal is {self.type}")

    def open(self):
        print("We are open!")

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []
        self.all_flavors = 31

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")
        
    def total_flavors(self):
        print(f"We have a total of {self.all_flavors} flavors")


