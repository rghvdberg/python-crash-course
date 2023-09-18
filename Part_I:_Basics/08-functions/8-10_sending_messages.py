# ┌──────────────────────────────────────────────────────────────────────────────┐
# │8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.  │
# │Write a function called send_messages() that prints each text message and     │
# │moves each message to  a new list called sent_messages as it’s printed. After │
# │Aftercalling the function, print both of your lists to make sure the messages │
# │were moved correctly.                                                         │
# └──────────────────────────────────────────────────────────────────────────────┘
def print_messages(messages):
    for message in messages:
        print(message)


def send_messages(messages):
    while messages:
        m = messages.pop()
        sent_messages.append(m)


messages = [
    "Hello!",
    "How are you?",
    "Hey!",
    "I'm doing fine.",
]
sent_messages = []
send_messages(messages)

print("Messages:")
print_messages(messages)

print("Sent Messages:")
print_messages(sent_messages)
