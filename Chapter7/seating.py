seating = input("How many people are in your dinner party? ")
seating = int(seating)

if seating <= 8:
    print("Your table is ready, please follow me.")
else:
    print("Please wait in the lounge until a table is available.")