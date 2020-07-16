banned_users=['andrew', 'sally','dave','david','sandra']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post")


print(banned_users[0])
for i in banned_users:
    print(i)


    