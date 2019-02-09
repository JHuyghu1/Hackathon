import turtle
import random
import lsystem

def getRules():
    fn = "Rules" + str(random.randint(1,2)) + ".txt"
    return fn

def colorTurtle():
    wn = turtle.Screen()
    wn.exitonclick()

def main():
    word = input("Please enter a three letter word: ")
    colorList = []
    for i in word:
        colorList += [ord(i)//16,ord(i)%16]
        #print("Decimal value: ", ord(i))
        #print("Hex value: ", ord(i)//16, ord(i)%16)
    print(len(colorList))
    for i in range(0, (len(colorList)//2)+1, 2):
        print(colorList[i:i+2], end = "")
    print(" ")
    for i in range(len(colorList)):
        print(colorList[i], end = "")
    print(" ")
    sys = lsystem.Lsystem("Rules1.txt")
    #colorTurtle()

main()
