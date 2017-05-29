import risar
import turtle


class Maze():
    # od okvirja min 25 px
    def __init__(self):
        self.maxX = 800
        self.maxY = 600
        risar.maxX = self.maxX
        risar.maxY = self.maxY
        risar.barvaOzadja(risar.crna)

    def stop(self):
        risar.stoj()

    def ogrodje(self):
        rightX = self.maxX - 25
        rightY = self.maxY - 145
        risar.crta(25, 25, rightX, 25, risar.bela, 3)
        risar.crta(rightX, 25, rightX, rightY, risar.bela, 3)
        risar.crta(24, 26, 25, rightY, risar.bela, 3)
        risar.crta(24, rightY, rightX, rightY, risar.bela, 3)


m = Maze()
m.ogrodje()
zelve = []

for i in range(5):
    i = turtle.Turtle()
    zelve.append(i)
import random

while True:
    a = random.randint(1, 2)
    if a == 1:
        for zelva in zelve:
            zelva.hide()
            if zelva.x >= 800 - 30 or zelva.y >= 600 - 150 or zelva.x <= 0 + 30 or zelva.y <= 0 + 30:
                zelva.turn(180)
                zelva.forward(25)
            else:
                rSpeed = random.randint(1, 10)
                rAngle = random.randint(5, 10)
                zelva.forward(rSpeed)
                zelva.turn(rAngle)
    if a == 2:
        for zelva in zelve:
            if zelva.x >= 800 - 30 or zelva.y >= 600 - 150 or zelva.x <= 0 + 30 or zelva.y <= 0 + 30:
                zelva.turn(180)
                zelva.forward(25)
            else:
                rSpeed = random.randint(1, 10)
                rAngle = random.randint(5, 10)
                zelva.forward(rSpeed)
                zelva.turn(-rAngle)
