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
    sys.createLsystem(jeff,color)
    sys.drawLSystem(jeff)
    wn.exitonclick()

def main():
    words = []
    colorList = []
    for i in range(3):
        words = [input("Please enter a three letter word: ")]
    for i in words:
        colorList += [(ord(word[i])//16) * 10 + ord(word[i])%16]
    color = (colorList[0], colorList[1], colorList[2])
    print(color)

    #colorTurtle(color)

main()
