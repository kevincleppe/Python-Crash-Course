class User:
    def __init__(self,first,last, username, password):
        self.first=first
        self.last=last
        self.username=username
        self.password=password
        self.login_attemts=0

    def describe(self):
        print(f"{self.first} {self.last} username is {self.username} and their password is {self.password}")

    def increment_login(self,login_attemts):
        self.login_attemts=login_attemts+1


kevin=User('kevin','cleppe','cleppster','password')
devin=User("devin","leppy","dleppy","passssss")

kevin.describe()
devin.describe()