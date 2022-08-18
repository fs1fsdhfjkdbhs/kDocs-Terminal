from time import sleep as wait

points = 0

wait(2)
print("Welcome to the game!")
wait(3)
print("This game is going to be a math quiz, so get your calculator ready!")
wait(3)
print("Okay, now, enjoy your quiz!")
wait(5)
q1 = input("What is 23 + 89? ")
if q1 == 112:
    print("Correct!")
    points += 1
else:
    print("Wrong!")
q2 = input("What is 45 x 12? ")
if q2 == 540:
    print("Correct!")
    points += 1
else:
    print("Wrong!")
q3 = input("What is 1207 + 2445? ")
if q3 == 3652:
    print("Correct!")
    points += 1
else:
    print("Wrong!")
q4 = input("What is 30 - 23? ")
if q4 == 7:
    print("Correct!")
    points += 1
else:
    print("Wrong!")
q5 = input("What is 15 ÷ 3? ")
if q5 == 5:
    print("Correct!")
    points += 1
else:
    print("Wrong!")
q6 = input("What is 1243 + 3849? ")
if q6 == 5092:
    print("Correct!")
    points += 1
else:
    print("Wrong!")
q7 = input("What is 342 - 893? ")
if q7 == -551:
    print("Correct!")
    points += 1
else:
    print("Wrong!")
q8 = input("What is 927 - 812")
if q8 == 115:
    print("Correct!")
    points += 1
else:
    print("Wrong!")
q9 = input("What is 786 + 1000? ")
if q9 == 1786:
    print("Correct!")
    points += 1
else:
    print("Wrong!")
q10 = input("Final question! What is 7896 - 2354? ")
if q10 == 5542:
    print("Correct! Results will be on in a few seconds..")
    points += 1
else:
    print("Wrong! Results will be on in a few seconds..")

wait(3)

print("You got {}/10 questions correct!".format(points))
