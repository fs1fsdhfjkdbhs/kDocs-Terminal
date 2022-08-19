#Settings

import playsound
from time import sleep as wait
import pyautogui

#Commands

commandLine = input("∂ ")
cmdPRINT = "print"
cmdMUSICLIST = "music.list"
cmdMUSIC = "music.Play"
cmdMUSICHELP = "music.help"
cmdHELP = "help"
cmdPING = "ping"
cmdPASSCHANGE = "pass.change"
cmdGAME = "game.py"

if commandLine == cmdPRINT:
    PRINT_RESULT = input("Please enter what you want to print: ")
    if PRINT_RESULT == "":
        print("ERROR: Cannot print nothing. (ERROR CODE 1296)")
        print("Please re-run the script for another command.")
    else:
        pyautogui.write(PRINT_RESULT, interval = 0.01)
        pyautogui.press('enter')
        wait(0.1)
        print("Please re-run the script for another command.")


if commandLine == cmdMUSICLIST:
    print("1. KING KONG - MHD, ID: 12906438\n2. Magnolia - Playboi Carti, ID: 23720508\n3. Sin Señal - Quevedo, Ovy On the Drums, ID: 90646806 \n4. Bad Habits - Ed Sheeran, ID: 02834983")
    print("Please re-run the script for another command.")

if commandLine == cmdMUSIC + ":12906438":
    print('Playing "KING KONG - MHD"')
    playsound.playsound('/kDocs-Terminal/music/KING KONG - MHD.mp3')
elif commandLine == cmdMUSIC + ":23720508":
    print('Playing "Magnolia - Playboi Carti"')
    playsound.playsound('/kDocs-Terminal/music/Magnolia - Playboi Carti.mp3')
elif commandLine == cmdMUSIC + ":90646806":
    print('Playing "Sin Señal - Quevedo, Ovy on the Drums"')
    playsound.playsound('/kDocs-Terminal/music/Sin Señal - Quevedo, Ovy on the Drums.mp3')
elif commandLine == cmdMUSIC + ":02834983":
    print('Playing "Bad Habits - Ed Sheeran"')
    playsound.playsound('/kDocs-Terminal/music/Ed Sheeran - Bad Habits.mp3')

if commandLine == cmdMUSICHELP:
    print("This is some info about the music commands.")
    print("1. music.list \nThis command is used to see what songs you can play, along with their ID.")
    print("2. music.Play \nThis command is used to play music, to use it, you have to do the following:\n   1. Run the script \n   2. Type 'music.Play:90646806'. The numbers are the ID of the song.")
    print("3. music.help \nThis command is used to get help with the music commands.")

if commandLine == cmdHELP:
    print("1. 'print'\nThis command is used to make the computer say things.\n2. 'music.help'\nThis command is used to get help with music commands.")
    print("3. 'music.Play'\nThis command is used to play music, use 'music.help' to learn how to use this command.\n4. 'music.list'\nThis command is used to see the list of available songs, you can put on your own songs.")
    print("To run more commands, you have to re-run the script.")

if commandLine == cmdPING:
    print("Pong!")
    print("Please re-run the script for another command.")

if commandLine == cmdPASSCHANGE:
    print("To change your password, go to the loading.py script in the 'scripts' folder, then find the password variable and change '1helesa' to the password you desire.")

if commandLine == cmdGAME:
    ars = input("Are you sure you want to go to the games tab? ('yes' if yes, 'no' if no) ")
    if ars == 'yes':
        import game
    elif ars == 'no':
        print("Loading canceled.")
