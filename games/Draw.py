from turtle import *
import random

game = input("wanna play a game?")

if game == "yes":
    print("press d to move with a line. press p to move without a line.\n")
    print("press r to make line red.\n")
    print("press g to make the line green\n")
    print("press b to make the line blue.\n")
    print("press e to erase")

else:
    print("go to python.org boi")

print("make a ")

things = ["3d square", "name", "circle"]

thing = things[random.randint(0,2)]

print(thing)


Screen()
showturtle()

wn = getscreen()
turty = getturtle()

def move():
    wn.onclick(goto)

def erase():
    reset()
    showturtle()

def change_to_red():
    turty.color("red")

def change_to_green():
    turty.color("green")

def change_to_blue():
    turty.color("blue")

def pu():
    turty.penup()

def pd():
    turty.pendown()

move()
onkey(erase, "e")
onkey(change_to_red, "r")
onkey(change_to_green, "g")
onkey(change_to_blue, "b")
onkey(pu, "p")
onkey(pd, "d")
listen()
mainloop()




          
