# za vsako črto ki jo narediš moraš pobrat koordinate, pol iz tega sestavš array
# koordinat, in v eni neskončni zanki pred premikom vedno preveriš vse kolizije
import risar
from turtle import Turtle


class Create_Room():
    def __init__(self):
        self.minX, self.maxX = 50, 750
        self.minY, self.maxY = 50, 450
        self.oknoX, self.oknoY = 800, 600
        self.koordinate = []
        self.objekti_koordinate = []

    def naredi_okvir(self):
        self.barva = risar.bela
        self.sirina = 3
        # prva črta, zgornja
        risar.crta(self.minX, self.minY, self.maxX, self.minY,
                   self.barva, self.sirina)
        # druga črta po levi strani
        risar.crta(self.minX, self.minY, self.minX, self.maxY,
                   self.barva, self.sirina)
        # tretja črta spodaj
        risar.crta(self.minX, self.maxY, self.maxX, self.maxY,
                   self.barva, self.sirina)
        # zadnja črta desno
        risar.crta(self.maxX, self.minY, self.maxX, self.maxY,
                   self.barva, self.sirina)
        self.koordinate.append([self.minX, self.maxX, self.minY, self.maxY])

    def dodaj_pregrado(self, x0, y0, x1, y1):
        risar.crta(x0, y0, x1, y1, self.barva, self.sirina)
        self.objekti_koordinate.append([x0, x1, y0, y1])


from random import randint

a = Create_Room()
a.naredi_okvir()
# t=Turtle()
toClose = 10
'''
self.minX,self.maxX = 50,750
self.minY,self.maxY = 50,450
self.oknoX,self.oknoY = 800,600
'''
# a.dodaj_pregrado(450,50,450,150)
counter = 0
zelve = []


def makeTurtles():
    for i in range(1):
        i = Turtle()
        zelve.append(i)


makeTurtles()
while True:
    counter += 1
    swearwords = ["Fuck", "cunt", "shit", "faggot", "retard", "MONKEY"]
    hitrost = randint(1, 5)
    kot = randint(1, 5)
    words = randint(0, 5)
    for z in zelve:
        for koordinate in a.koordinate:
            # minx,maxx,miny,maxy
            wX, wY = z.x, z.y
            if z.x - toClose <= koordinate[0]:
                z.turn(kot + 75)
                z.forward(5)
                makeTurtles()
                risar.besedilo(wX, wY, swearwords[words], risar.nakljucna_barva(), hitrost ** kot)
            elif z.x + toClose >= koordinate[1]:
                z.turn(kot + 75)
                z.forward(5)
                risar.besedilo(wX, wY, swearwords[words], risar.nakljucna_barva(), hitrost ** kot)
            elif z.y - toClose <= koordinate[2]:
                z.turn(kot + 75)
                z.forward(5)
                makeTurtles()
                risar.besedilo(wX, wY, swearwords[words], risar.nakljucna_barva(), hitrost ** kot)
            elif z.y + toClose >= koordinate[3]:
                z.turn(kot + 75)
                z.forward(5)
                makeTurtles()
                risar.besedilo(wX, wY, swearwords[words], risar.nakljucna_barva(), hitrost ** kot)

        rnd = randint(1, 2)
        z.forward(hitrost)
        if rnd == 1:
            z.turn(kot)
        elif rnd == 2:
            z.turn(-kot)
        counter += 1
        if counter == 10000:
            break
