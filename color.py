import turtle

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
    for i in range(len(colorList)):
        print(colorList[i], end = "")
    print(" ")
    colorTurtle()

main()
