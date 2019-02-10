import turtle
import random
import lsystem

"""
    Randomizes which lsystem rules are passed
    args: None
    return: fn (string)
"""
def randRules():
    fn = "Rules" + str(random.randint(1,2)) + ".txt"
    return fn

"""
    Creates the turtle (Jeff) and screen
    args: color (tuple of ints)
    return: None
"""
def colorTurtle(color):
    wn = turtle.Screen()
    wn.colormode(255)
    jeff = turtle.Turtle()
    jeff.pencolor(color)
    wn.exitonclick()

def main():
    word = input("Please enter a three letter word: ")
    colorList = []
    for i in word:
        colorList += [(ord(i)//16) * 10 + ord(i)%16]
    color = (colorList[0], colorList[1], colorList[2])
    print(color)
    sys = lsystem.Lsystem(randRules())
    colorTurtle(color)

main()
