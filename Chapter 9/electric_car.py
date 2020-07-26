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


class Battery:
    def __init__(self,battery_size=75):
        self.battery_size=battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size} % charge")

    def get_range(self):
        if self.battery_size ==75:
            range =260
        elif self.battery_size==100:
            range=315

        print(f"This car can go {range} miles on a full charge")

class Electric(Car):

    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.odometer=200
        self.battery_size=75
        self.battery=Battery()

    def describe_battery(self):
        print(f"This car has {self.battery_size} % left!")

    def fill_gas_tank(self):
        print("This car does not need gas!")

my_tesla=Electric('tesla','model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.read_odometer()
mycar=Car("toyota","prius", 2015)
print(mycar.get_descriptive_name())        
mycar.read_odometer()
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()