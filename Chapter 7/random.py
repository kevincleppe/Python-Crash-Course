import random

num = random.randint(1,10)
tries = 1
guess = 0

guess = int(input("Guess a number from 1 to 9: "))

while guess != num:
    if guess == num:
        tries = tries + 1
        break
    elif guess == str('Exit'):
        break
    elif guess > num:
        guess = int(input("Too high! Guess again: "))
        tries = tries + 1
        continue
    else:
        guess = int(input("Too low! Guess again: "))
        tries = tries + 1
        continue

print("Exactly right!")
print("You guessed " + str(tries) + " times.")