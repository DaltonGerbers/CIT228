filename = "learning_python.txt"

with open(filename) as learning_python:
    contents = learning_python.read()
print("-------------Output from read()-------------")
print(contents)

print("-------------Output from the loop inside with...open-------------")
with open(filename) as learning_python:
    for line in learning_python:
        print(line)

print("-------------Output from readlines()-------------")
with open(filename) as learning_python:
    content_list = learning_python.readlines()
print("Original list=",content_list)
for line in content_list:
    print(line)

print("-------------Replacing In Python you can...with in C# you cannot (except the first one)-------------")
counter = 0
with open(filename) as learning_python:
    for line in learning_python:
        if (counter > 0):
            print("Original: ", line)
            print("Modified: ", line.replace("In Python you can", "In C# you cannot"))
        else:
            print("Original: ", line)
            print("Modified: ", line.replace("In Python you can", "In C# you can"))
            counter += 1