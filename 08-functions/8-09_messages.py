# ┌─────────────────────────────────────────────────────────────────────────────────┐
# │ 8-9. Messages: Make a list containing a series of short text messages. Pass the │
# │ list to a function called show_messages(), which prints each text message.      │
# └─────────────────────────────────────────────────────────────────────────────────┘


def show_messages(messages):
    for message in messages:
        print(message)


# a list of short text messages

messages = [
    "Hello!",
    "How are you?",
    "Hey!",
    "I'm doing fine.",
]

# call function
show_messages(messages[:])
