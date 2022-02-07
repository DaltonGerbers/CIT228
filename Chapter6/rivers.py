rivers={
    "Colorado":"United States",
    "Rio Grande":["Mexico", "United States"],
    "Ural":["Kazakhstan", "Russia"]
}

print("------------------Rivers & Countries------------------")
for key,value in rivers.items():
    print(f"The {key.title()} river flows through {value}")
print("------------------Rivers------------------")
for key in rivers.keys():
    print(key.title())
print("------------------Countries------------------")
for value in rivers.values():
    print(value)