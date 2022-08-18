from time import sleep as wait
from playsound import playsound as sound

wait(3)
print("Welcome to the Games Tab!")
wait(2)
print("To start, type '/start' in the upcoming input.")
wait(2)
print("Okay, now enjoy some games!")

wait(2)
gCHOOSE = input("Enter a shortcut for games, we will add more in the future! ")

if gCHOOSE == "/start":
    sound('/Users/nipeal/Desktop/beep.mp3')
    wait(1)
    import mathQuiz

