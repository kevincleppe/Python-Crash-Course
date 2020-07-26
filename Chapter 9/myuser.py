from ch9_7 import *


devin=User("devin","leppy","dleppy","passssss")
devin.describe()
kevin=Admin('kevin','cleppe','cleppster','password')
dave=Basic("david", "smith", "dsmith", "mypass",112100)

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