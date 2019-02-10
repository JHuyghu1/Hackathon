import turtle
import random
import lsystem

"""
    Creates the turtle (Jeff) and screen
    args: color (tuple of ints)
    return: None
"""
def colorTurtle(color):
    wn = turtle.Screen()
    wn.colormode(255)

    jeff = turtle.Turtle()
    jeff.shape("turtle")
    jeff.pencolor(color)
    #jeff.pensize(5)
    jeff.setpos(-325,325)
    jeff.speed(0)
    
    sys = lsystem.Lsystem("Rules3.txt")
    sys.createLsystem()
    sys.drawLSystem(jeff)
    wn.exitonclick()

def main():
    word = input("Please enter a three letter word: ")
    colorList = []
    for i in word:
        colorList += [(ord(i)//16) * 10 + ord(i)%16]
    color = (colorList[0], colorList[1], colorList[2])
    print(color)

    colorTurtle(color)

main()
