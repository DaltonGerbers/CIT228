glossary={
    "dictionary":"Python data type which stores key value pairs",
    "python":"a general-purpose programming language emphasizing code readability with its use of indentation.",
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
    print(key.title())
    print("\t",value)