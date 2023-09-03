from random import choice

tickets = (
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "a",
    "b",
    "c",
    "d",
    "e",
)
winning_tickets = []
while len(winning_tickets) < 4:
    new_ticket = choice(tickets)
    if new_ticket not in winning_tickets:
        winning_tickets.append(new_ticket)
        print(f"The winning ticket is {new_ticket}")


print(winning_tickets)

counter = 0
winner = False
while not winner:
    counter += 1
    ticket_drawn = choice(tickets)
    print(f"Number of draws: {counter}")
    print(f"You have drawn ticket {ticket_drawn}")
    if ticket_drawn in winning_tickets:
        winner = True
        print("You have won!")
    else:
        print(f"Sorry, {ticket_drawn} is not one of the winning tickets")
