# ┌──────────────────────────────────────────────────────────────────────────────────┐
# │8-11. Archived Messages: Start with your work from Exercise 8-10. Call the func-  │
# │tion send_messages() with a copy of the list of messages. After calling the func- │
# │tion, print both of your lists to show that the original list has retained its    │
# │messages.                                                                         │
# └──────────────────────────────────────────────────────────────────────────────────┘
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
send_messages(messages[:])

print("Messages:")
print_messages(messages)

print("Sent Messages:")
print_messages(sent_messages)
