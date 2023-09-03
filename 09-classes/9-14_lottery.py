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
