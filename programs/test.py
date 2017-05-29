from turtle import *
from random import randint
def shapes(zelva):
    var=10
    while True:
        sh = randint(1, 5)
        if zelva.x>=risar.maxX-25:
            zelva.x=0
            zelva.y+=10
        else:
            zelva.x+=10
            zelva.y+=0
        if sh==1:
            for i in range(16):
                zelva.forward(5)
                if i%2==0:
                    zelva.turn(90)
                else:
                    zelva.turn(-45)
        if sh==2:
            for i in range(16):
                zelva.forward(5)
                zelva.turn(35)
        if sh==3:
            for i in range(4):
                zelva.forward(5)
                zelva.turn(90)
        if sh==4:
            for i in range(30):
                zelva.forward(5)
                zelva.turn(3*i)
        if sh==5:
            for i in range(30):
                zelva.forward(-5)
                zelva.turn(3*-i)

        var+=5
t=Turtle()
shapes(t)