from random import choice
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket=[]
def create_winning_ticket(possibilities):
    
    while len(winning_ticket) < 4:
        picked_number=choice(possibilities)
        if picked_number not in winning_ticket:
            winning_ticket.append(picked_number)
    print(f"Winning ticket is {winning_ticket}")

    return winning_ticket


def check_ticket(played_ticket, winning_ticket):
    # Check all elements in the played ticket. If any are not in the 
    #   winning ticket, return False.
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket!
    return True


def make_random_ticket(possibilities):
    ticket=[]
    while len(ticket) < 4:
        i=choice(possibilities)
        if i not in ticket:
            ticket.append(i)
    print(f"Random ticket is {ticket}")

    return ticket

count = 0

won = False
winning_ticket=create_winning_ticket(possibilities)

while not won:
    print("Making new ticket")
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    count += 1
    

if won:
    print("We have a winning ticket!")
    print(f"Took aapprox {count} tries")
    print(winning_ticket)
    print(new_ticket)

else:
    print(f"Tried {count} times, without pulling a winner. :(")