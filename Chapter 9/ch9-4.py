class Restaurant:
    def __init__(self, food_type, describe):
        self.type= food_type
        self.describe = describe
        self.number_served=0

    def decribe_restaurant(self):
        print(f"The restaurant is {self.describe} and our best meal is {self.type}")

    def open(self):
        print("We are open!")

    def set_number_served(self, number_served):
        self.number_served= number_served
        

    def updated_number_served(self,update_served):
        self.number_served += update_served
        print(f"{self.number_served} {update_served}")
    
    def quarantine(self, quarantine):
        self.number_served /= quarantine
    

zutto=Restaurant("sushi", "Japanese")
zutto.decribe_restaurant()
zutto.open()
zutto.number_served = 38
print(f"Number served: {zutto.number_served}")
zutto.set_number_served(111)
print(f"Number served: {zutto.number_served}")
zutto.updated_number_served(323)
print(f"Number served: {zutto.number_served}")
zutto.quarantine(333)
print(f"Number served: {zutto.number_served}")

