import turtle
from easygui import *

color = buttonbox("What color do you want?", choices= ["red", "blue", "pink"])
turtleshape = buttonbox("What shape turtle do you want?", choices= ["turtle",  "arrow", "square"])
shape = buttonbox("What shape should the turtle draw?", choices= ["square", "circle", "spiral"])

turtle.color(color)
turtle.shape(turtleshape)

if shape=="square" :
    for i in range(4) :
        turtle.forward(100)
        turtle.right(90)

elif shape=="circle" :
    turtle.circle(100)

else :
   for i in range(1000000000000000) :
       turtle.stamp()
       turtle.forward(i)
       turtle.right(24)
