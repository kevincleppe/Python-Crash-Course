class Dog:
    def __init__(self,name,age,treat):
        self.name = name
        self.age = age
        self.treat =treat
        
    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over!")

    def want_treat(self):
        print(f"{self.name} wants a treat! Their favorite treat is {self.treat}")


my_dog = Dog('Robin', 10, "bread")
print(f"My dog's name is {my_dog.name}.")
print(f"My dog {my_dog.name} is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()
my_dog.want_treat()