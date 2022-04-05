import re
import os
import turtle
from PIL import Image


class Fractaler():
    def __init__(self, axim, newF, newB, level, angle):
        self.axim = axim
        self.newF = newF
        self.newB = newB
        self.level = level
        self.rotateAngle = angle
        self.Fractal()

    def SaveToPNG(self, level):
        img = Image.open(str(level) + ".eps")
        img.save("Level-" + str(level + 1) + ".png")
        os.remove(os.getcwd() + "/" + str(level) + ".eps")

    def DrawResult(self, level):

        window = turtle.Screen()
        window.setup(2560, 1660)
        window.bgcolor('white')
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.color('black')
        pen.penup()
        pen.setpos(0, 0)
        pen.speed(10)

        for letter in self.axim:
            if letter == "F" or letter == "f":
                pen.pendown()
                pen.forward(3)

            if letter == "B" or letter == "b":
                pen.penup()
                pen.forward(3)

            if letter == "+":
                pen.left(self.rotateAngle)

            if letter == "-":
                pen.right(self.rotateAngle)

        pen.getscreen().getcanvas().postscript(file=str(level) + ".eps")
        pen.clear()

    def PrintResult(self, level):
        print("Level", level + 1, ": ", self.axim)

    def Calculate(self):
        newWord = "\0"
        for letter in self.axim:
            if letter == "F" or letter == "f":
                newWord = newWord + self.newF
            if letter == "B" or letter == "b":
                newWord = newWord + self.newB
            if letter == "+":
                newWord = newWord + "+"
            if letter == "-":
                newWord = newWord + "-"
        self.axim = newWord
        newWord = "\0"

    def Fractal(self):
        for i in range(self.level):
            self.Calculate()
            self.PrintResult(i)
            self.DrawResult(i)
            self.SaveToPNG(i)


class InputAndCheck():
    def __init__(self):
        self.axim = None
        self.newF = None
        self.newB = None
        self.level = None
        self.angle = None
        self.Input()

    def CheckChar(self):
        if self.axim != None:
            subString = re.sub("[^FfBb+-]", "", self.axim)
            if subString != self.axim:
                return False

        if self.newF != None:
            subString = re.sub("[^FfBb+-]", "", self.newF)
            if subString != self.newF:
                return False

        if self.newB != None:
            subString = re.sub("[^Bb]", "", self.newB)
            if subString != self.newB:
                return False

        return True

    def Input(self):
        while (True):
            self.axim = input("Input axim: ")
            if self.CheckChar():
                break
            else:
                print("axim is not a correct string !\n")

        while (True):
            self.newF = input("Input newF: ")
            if self.CheckChar():
                break
            else:
                print("newF is not a correct string !\n")

        while (True):
            self.newB = input("Input newB: ")
            if self.CheckChar():
                break
            else:
                print("newB is not a correct string !\n")

        while (True):
            try:
                self.level = int(input("Input level: "))
                break

            except ValueError:
                print("Level is not a integer !\n")

        while (True):
            try:
                self.angle = int(input("Input angle: "))
                break

            except ValueError:
                print("angle is not a integer !\n")


if __name__ == "__main__":
    input = InputAndCheck()
    fractal = Fractaler(input.axim, input.newF, input.newB, input.level,
                        input.angle)
