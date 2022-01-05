#!/usr/bin/env python3


score = 0
count = 0

while count < 3:
    answer = input("What city are the World Series champs from: ").capitalize()
    if answer == "Atlanta":
        print("Correct! on to question two")
        score += 1

        answer2 = input("What is the name of the NFL team from Seattle:").capitalize()
        if answer2 == "Seahawks":
            print("Correct! Now for the final question ")
            score += 1

        answer3 = input("In which Sport would you score a touchdown:").capitalize()
        if answer3 == "Football":
            print("Correct! you are a sports genius!")
            score += 1
            break

    else:
        print("Nope that is wrong. Try Again")
        count += 1

print("The correct answer to the questions are 1.Atlanta, 2.Seahawks and 3.Football!")
print("Your overall score is {" + str(score) + "}")
