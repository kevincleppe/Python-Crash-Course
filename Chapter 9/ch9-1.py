class Restaurant:
    def __init__(self, food_type, describe):
        self.type= food_type
        self.describe = describe

    def decribe_restaurant(self):
        print(f"The restaurant is {self.describe} and our best meal is {self.type}")

    def open(self):
        print("We are open!")


zutto=Restaurant("sushi", "Japanese")

zutto.decribe_restaurant()
zutto.open()