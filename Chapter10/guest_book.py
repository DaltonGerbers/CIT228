import random
import os

filename = "guest_book.txt"
"""with open(filename, 'a') as book:
    guest = input("Enter your name (q to quit): ")
    while (guest != "q" and guest != "Q"):
        book.write("\n" + guest)
        print("Welcome, " + guest + ", please enjoy your visit.")
        guest = input("Enter your name (q to quit): ")"""

if os.path.exists(filename):
    os.remove(filename)
rooms = []
with open(filename, 'w') as roomFile:
    guest = input("Enter your name (q to quit): ")
    while (guest != "q" and guest != "Q"):
        number = random.randint(1,100)
        while number in rooms:
            number = random.randint(1,100)
        print(f"{guest} you will stay in room number {number}")
        rooms.append(number)
        guest += ", room# " + str(number) + "\n"
        roomFile.write(guest)
        guest = input("Enter your name (q to quit): ")

with open(filename) as roomFile:
    print("-------------Guests & Rooms Assigned-------------\n")
    for line in roomFile:
        print(line)