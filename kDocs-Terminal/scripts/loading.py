from time import sleep as wait


print("Loading Script..")
wait(5)
print("Script Loaded!")
wait(2)
print("Loading Terminal..")
wait(7)
print("Terminal Loaded!")
wait(2)
print("Loading User Info..")
wait(6)
print("Player User Loaded!")
wait(2)
print("Loading kDocs Assets..")
wait(5)
print("kDocs Assets Loaded!")
wait(2)
print("Loading Files..")
wait(6)
print("Files Loaded!")
wait(2)
print("Connecting to C:Drive..")
wait(10)
print("C:Drive has been connected!")
wait(2)
print("Connecting Terminal With Computer Files..")
wait(12)
print("Terminal has connected with Files!")
wait(2)
print("Connecting..")
wait(6)
print("Connection has been successfull!")
wait(3)
securityTrial1 = input("Please enter your password to continue: ")
userPassword = "1helesa" #  <<<<  Change your password here

if securityTrial1 == userPassword:
    print("Checking output..")
    wait(5)
    print("Login Complete! Welcome to kDocs!")
    import scripts.cmds as cmds
else:
    print("Checking output..")
    wait(5)
    print("Login Imcomplete. ")
    wait(2)
    securityTrial2 = input("Please try again: ")
    if securityTrial2 == userPassword: 
        print("Checking output..")
        wait(5)
        print("Login Complete! Welcome to kDocs!")
        import scripts.cmds as cmds
    else:
        print("Checking output..")
        wait(5)
        print("Login Imcomplete.")
        wait(2)
        securityTrial3 = input("Please try again: ")
        if securityTrial3 == userPassword: 
            print("Checking output..")
            wait(5)
            print("Login Complete! Welcome to kDocs!")
            import cmds
        else:
            print("Checking output..")
            wait(5)
            print("Login Imcomplete, please run the file to try again.")
