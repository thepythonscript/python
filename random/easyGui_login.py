from easygui import *
users = {}
status = ""

while status != ("Quit"):
    status = buttonbox("Are you a registered user? press q to quit: ", choices=["Yes", "No", "Quit"])

    if status == ("No"):
        createlogin = enterbox("create a login name: ")

        if createlogin in users:
            msgbox ("Login name already exists!\n")
        else:
            createpassw = enterbox("Create password: ")
            users[createlogin] = createpassw
            msgbox("\nUser created!\n")

    elif status == ("Yes"):
        login = enterbox("Enter login name: ")

        if login in users:
            passw = passwordbox("Enter password: ")

            if passw == users[login]:
                msgbox("login successful!\n")

            else:
                msgbox("login unsuccessful")

        else:
            msgbox("User dosent exist")
