answer = ""
while (answer != "q" and answer != "Q"):
    a = ""
    b = ""
    isNotNum = True
    while (isNotNum):
        a = input("Please enter the first number ")
        try:
            a = int(a)
        except ValueError:
            print("You must enter numbers instead of text, please try again!")
        else:
            isNotNum = False
    isNotNum = True
    while (isNotNum):
        b = input("Please enter the second number ")
        try:
            b = int(b)
        except ValueError:
            print("You must enter numbers instead of text, please try again!")
        else:
            isNotNum = False
    answer = f"{a} + {b} = {a + b}"
    print(answer)
    answer = input("Would you like to play again? (q to quit)")