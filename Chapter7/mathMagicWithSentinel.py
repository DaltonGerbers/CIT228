import random
keepPlaying = input("Do you want to play? Enter \"q\" to quit")
numberCorrect = 0
while keepPlaying != "q":
    randNumber1 = random.randrange(1, 1000)
    randNumber2 = random.randrange(1, 1000)
    correctAnswer = int(randNumber1 + randNumber2)
    yourAnswer = int(input(f"What is the integer value of {randNumber1} + {randNumber2}?"))
    if correctAnswer==yourAnswer:
        print("Great job, you answered correctly!")
        numberCorrect+=1
    else:
        print("Oops, the correct answer is ",correctAnswer)
    keepPlaying = input("Do you want to keep playing? Enter \"q\" to quit")

print("You answered ", numberCorrect, "questions correctly!")
print("Thanks for playing!")