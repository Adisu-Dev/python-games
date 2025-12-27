print("\n\n Welcome to BDU Students Grading  system  ")
print(" Students result press -1 to exit from the program  ")
while True:
    user_input = input("\nplease enter your result (0-100) ")
    score = float(user_input)
    #  Exit condition
    if score == -1:
        print("Good bye! program terminated")
        break
    if score > 100 or score <= 0:
        print("Invalid input ⚠️ please enter from 0 to 100")
    elif score >= 90:
        print("Congratulations! you scored: A+")
    elif score >= 85:
        print("Congratulations! you scored: A")
    elif score >= 80:
        print(" You scored: A-")
    elif score >= 75:
        print(" you scored: B+")
    elif score >= 70:
        print(" you scored: B")
    elif score >= 65:
        print(" you scored: B-")
    elif score >= 60:
        print(" you scored: C+")
    elif score >= 50:
        print(" you scored: C")
    elif score >= 40:
        print(" you scored: D")
    else:
        print("I'm sorry🥲  you scored: F")
        print("You are failed😭😭😭")
