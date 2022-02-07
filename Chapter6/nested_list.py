rivers={
    "Colorado":"United States",
    "Rio Grande":["Mexico", "United States"],
    "Ural":["Kazakhstan", "Russia"]
}

for key,value in rivers.items():
    if type(value)==list:
        print(f"The {key.title()} river flows through: ")
        for v in value:
            print("\t\t\t\t",v)
    else:
        print(f"The {key.title()} rivier flows through {value.title()}")