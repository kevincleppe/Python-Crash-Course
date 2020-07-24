class User:
    def __init__(self,first,last, username, password):
        self.first=first
        self.last=last
        self.username=username
        self.password=password
        self.login_attemts=0

    def describe(self):
        print(f"{self.first} {self.last} username is {self.username} and their password is {self.password}")

    def increment_login(self):
        self.login_attemts +=1
        

    def reset_login(self):
        self.login_attemts=0

kevin=User('kevin','cleppe','cleppster','password')
devin=User("devin","leppy","dleppy","passssss")

kevin.describe()
devin.describe()
kevin.increment_login()
kevin.increment_login()
kevin.increment_login()
kevin.increment_login()
kevin.increment_login()

print(f"{kevin.login_attemts}")