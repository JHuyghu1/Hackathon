import turtle
import random
import lsystem

"""
    Creates the turtle (Jeff) and screen
    args: color (tuple of ints)
    return: None
"""
def colorTurtle(colors):
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor("black")

    jeff = turtle.Turtle()
    jeff.shape("turtle")
    jeff.pensize(5)
    jeff.penup()
    jeff.setpos(-325,325)
    jeff.pendown()
    jeff.speed(0)

    sys = lsystem.Lsystem("Rules3.txt")
    #jeff.pencolor(colors[i])
    sys.createLsystem()
    sys.drawLSystem(jeff,colors)
    wn.exitonclick()

def main():
    ''' Takes words from the user and changes them to the hex value - Adds 125 to make it lighter'''
    colorList = []
    while (len(colorList) < 9):
        word = input("Please enter a three letter word: ")
        if len(word) > 3:
            print("You idiot, I said 3-letter word")
        elif len(word) == 0:
            print("You idiot, enter a 3-letter word")
        else:
            for char in word:
                colorList += [(ord(char)//16) * 10 + (ord(char)%16 + 125)]
    #print(colorList)
    #print(len(colorList))
    rgbList = []
    for i in range(0, len(colorList), 3):
        (r,g,b) = (colorList[i], colorList[i+1], colorList[i+2])
        for i in range(3):
            if r > 200 and g < 200:
                b -= 50
            elif r <= 200:
                r += 50
            elif g >= 200:
                g -= 70
            else:
                b += 20
        rgbList += [(r,g,b)]
    #print(rgbList)
    colorTurtle(rgbList)

main()
