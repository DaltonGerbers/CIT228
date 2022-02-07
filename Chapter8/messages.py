def show_messages(list):
    for i in list:
        print(i)
def send_messages(list):
    sent_messages = []
    while list:
        current_messages = list.pop()
        print(current_messages)
        sent_messages.append(current_messages)
    print("messages:",list)
    print("sent messages:",sent_messages)


"""messages = ["This is a message.", "Here are some words.", "What, want another?"]
show_messages(messages)
print()
send_messages(messages[:])"""