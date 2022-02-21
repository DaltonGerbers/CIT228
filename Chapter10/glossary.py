import json

def menu():
    selection = int(input("1-create file, 2-read file, 3-add to file, 4-quit  "))
    while selection!=1 and selection!=2 and selection!=3 and selection!=4:
        print("You made an invalid selection, please try again")
        selection = int(input("1-create file, 2-read file, 3-add to file, 4-quit  "))
    return selection

def write(object):
    overwrite = input("You are about to create a new file, existing data will be overwritten (q to quit, any key to continue) ")
    if overwrite !="q":
        with open("glossary.json", "w") as write_file:
            json.dump(object, write_file, indent=4, sort_keys=True)
            print("glossary.json has been created")

def read():
    try:
        with open("glossary.json") as read_file:
            glossary = json.load(read_file)
    except FileNotFoundError:
        print("The file doesn't exist or cannot be found.")
        print("Please make a different menu selection")      
    else: 
        for key, value in glossary.items():
            print(key, ":", value)

def add(new_item):
    with open("glossary.json", "r+") as add_file:
        glossary = json.load(add_file)
        glossary.update(new_item)
        add_file.seek(0)
        json.dump(glossary, add_file, indent=4, sort_keys=True)
        print("Data has been added to glossary.json")

def get_key():
    words = input("Enter your word  ")
    words = words.split()
    word = ""
    piece = 0
    for i in words:
        if piece == 0:
            word += words[piece].lower()
        else:
            word += words[piece].title()
        piece += 1
    return word

def get_value():
    definition=input("Enter the definition of the word  ")
    return definition

glossary={
    "dictionary":"Python data type which stores key value pairs",
    "python":"a general-purpose programming language emphasizing code readability with its use of indentation",
    "list":"a storage medium that stores a list of variables",
    "variable":"a storage medium that stores one piece of data of a single type at a time",
    "tuple":"a list of items that do not change",
    "print":"a method used to display an output to the user",
    "loop":"a method used to repeat a segment of code until a certain condition is met",
    "boolean":"a type of variable that stores either true or flase",
    "concatenation":"a method of joining string or non-string variables together",
    "class":"a method of creating a user defined object (I took a previous course for Python and I really cannot think of any other terms we have learned thus far so I will use this)"
}

for key,value in glossary.items():
    print(key)
    print("\t",value)
choice=menu()
while choice != 4:
    if choice == 1:
        write(glossary)
    elif choice == 2:
        read()
    elif choice == 3:
        word = get_key()
        definition = get_value()
        new_dictionary_entry = {word:definition}
        add(new_dictionary_entry)
    else:
        print("The option you selected is not available, please try again")        
    choice=menu()