class Car:
    def __init__(self, make,model,year):
        self.make=make
        self.model=model
        self.year=year 

    def get_descriptive_name(self):
        print(f"This is a test {self.model}")
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
        print(f"{long_name}")
        print(f"hmm {self.year}")

my_new_car = Car('toyota', 'prius', 2015)
print(my_new_car.get_descriptive_name())
my_new_car.get_descriptive_name()