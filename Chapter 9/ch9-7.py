class User():
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


class Admin(User):
    def __init__(self, first, last, username, password):
        super().__init__(first, last, username, password)
        self.privs=[]

    def show_privileges(self):
        print("\nThe admin has the following privileges: ")
        for i in self.privs:
            print(f"-- {i}")

class Basic(User):
    def __init__(self, first, last, username, password, friends):
        super().__init__(first,last,username,password)
        self.basic=[]
        self.friends = friends
    
    def num_of_friends(self, friends):
        print(f"\nThis user has {self.friends} friends")

    def show_basic_privileges(self):
        print("\nBasic users can do the following: ")
        for i in self.basic:
            print(f"-- {i}")

class Privileges():
    def __init__(self, privs=[]):
        self.privilege=privilege 

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privilege:
            for i in self.privilege:
                print(f"- {i}")
        else:
            print("- This user has no privileges.")


kevin=Admin('kevin','cleppe','cleppster','password')
devin=User("devin","leppy","dleppy","passssss")
kevin.privs=[
    'can delete accounts',
    'can reset passwords',
    'can create new accounts',
]

dave=Basic("david", "smith", "dsmith", "mypass",112100)
dave.basic =[
    'create account',
    'post update',
    'deactivate account',
]
kevin.describe()
devin.describe()
kevin.show_privileges()
dave.show_basic_privileges()
dave.num_of_friends(1)