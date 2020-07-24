class Car:
    def __init__(self, make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer = 0 

    def get_descriptive_name(self):
        long_name=f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it")

    def update_odom(self, milage):
        if milage >= self.odometer:
            self.odometer=milage
        else:
            print(f"Cannot roll back the odom {self.odometer} > {milage}")

    def increment(self, miles):
        self.odometer+=miles
mycar=Car("toyota","prius", 2015)

print(mycar.get_descriptive_name())        
mycar.read_odometer()
mycar.odometer=33
mycar.read_odometer()
mycar.update_odom(2)
mycar.read_odometer()
mycar.increment(100)
mycar.read_odometer()
