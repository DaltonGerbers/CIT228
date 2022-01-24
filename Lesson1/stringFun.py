# excercise 1 - use your own first and last name
print("-----------------------------------------------")
print("Exercise 1")
name = "Dalton Gerbers"
print(name.title())
print(name.upper())
print(name.lower())
print("My first initial is: ", name[0].upper())

# exercise 2 - make up your own noun your own noun, adjective, verb, and ending
# use concatenation to create sentence 1
# use an f-string to create sentence2
print("-----------------------------------------------")
print("Exercise 2")
noun = "student"
adj = "CIT"
verb = "finished"
ending = "an hour before it was due."
sentence1 = "the lazy " + adj + " " + noun + " " + verb + " " + ending
sentence2 = f"the lazy {adj} {noun} {verb} {ending}"
print(sentence1.upper())
print(sentence2.lower())

# exercise 3 - 
print("-----------------------------------------------")
print("Exercise 3")
theRaven = """
Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
“’Tis some visitor,” I muttered, “tapping at my chamber door—
            Only this and nothing more.”
            
    Ah, distinctly I remember it was in the bleak December;
And each separate dying ember wrought its ghost upon the floor.
    Eagerly I wished the morrow;—vainly I had sought to borrow
    From my books surcease of sorrow—sorrow for the lost Lenore—
For the rare and radiant maiden whom the angels name Lenore—
            Nameless here for evermore."""
print(theRaven)

# exercise 4 - 
print("-----------------------------------------------")
print("Exercise 4")
print("Classics\t\t\tModern\n")
print("Scooby Doo\t\t\tMicky Mouse Clubhouse\n")
print("Flintstones\t\t\tPAW Patrol\n")
print("Jetson\t\t\t\tPJ Masks\n")