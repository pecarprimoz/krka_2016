from math import sqrt
from random import randint

'''
#TODO:
custom room shape, random room shape?
'''


class room_creation():
    def __init__(self, dim):
        self.dim = dim
        self.room = [[' ' for i in range(self.dim)] for j in range(self.dim)]

    def create_room(self, wall_length):
        # create walls in x,y axis
        # create for x axis; starting coordinates 0,0
        for i in range(wall_length):
            self.room[0][i] = '*'
        for j in range(wall_length):
            self.room[wall_length][j] = '*'
        # create walls for y axis;starting 0,0
        for k in range(wall_length):
            if k + 1 != len(self.room) - 1:
                self.room[k + 1][0] = '*'
        for h in range(wall_length):
            if h + 1 != len(self.room) - 1:
                self.room[h + 1][wall_length - 1] = '*'

    # returns created room
    def create_maze_pillar(self):
        yAxis = randint(2, self.dim - 3)
        xAxis = randint(2, self.dim - 4)
        if self.room[yAxis][xAxis] != "*":
            right = False
            left = False
            counter = 0
            tempY = yAxis
            while self.room[tempY][xAxis + 1] != "*":
                counter += 1
                tempY += 1
            if counter + yAxis == tempY:
                right = True
                counter = 0
                tempY = yAxis
            while self.room[tempY][xAxis - 1] != "*":
                counter += 1
                tempY -= 1
            if counter + yAxis == tempY:
                left = True
            if left and right:
                if yAxis >= 4:
                    while yAxis != 0:
                        self.room[yAxis][xAxis] = "*"
                        yAxis -= 1
                elif yAxis <= 4:
                    while yAxis != self.dim - 1:
                        self.room[yAxis][xAxis] = "*"
                        yAxis += 1
        else:
            self.create_maze_pillar()

    def output_room(self):
        # output in string form, print all chars in array
        myRoom = ""
        for col in self.room:
            myRoom += " ".join(col) + "\n"
        print(myRoom)

    def room_array(self):
        return self.room


class Dummy():
    def __init__(self, myRoom):
        # starting position
        self.x, self.y = 1, 1
        self.looks = "@"
        # self.defaultMov="L" #currently unused
        # need a place to move around, take array from room_cretion class
        self.area = myRoom
        # coordinates for room length calculation
        self.endCoordinates = []

    def setUp(self):
        # put myself on index 1,1 in array self.area
        self.area[1][1] = self.looks

    def moveL(self, x, y):
        # change the area I was before to blank, update next area with me
        self.area[y][x] = ' '
        self.area[y][x - 1] = self.looks

    def moveR(self, x, y):
        self.area[y][x] = ' '
        self.area[y][x + 1] = self.looks

    def moveU(self, x, y):
        self.area[y][x] = ' '
        self.area[y - 1][x] = self.looks

    def moveD(self, x, y):
        self.area[y][x] = ' '
        self.area[y + 1][x] = self.looks

    def output_room(self):
        # output in string form, print all chars in array
        myRoom = ""
        for col in self.area:
            myRoom += " ".join(col) + "\n"
        print(myRoom)

    def update(self):
        # add starting point to coordinates
        coordinates = [(1, 1)]
        self.setUp()
        self.output_room()
        while True:
            # if current y and x+1 is empty, then can move there; x axis right
            while self.area[self.y][self.x + 1] != "*":
                # update my coordinates, increse x by 1
                self.moveR(self.x, self.y)
                self.x += 1
                # draw my current position
                self.output_room()
            # after moving to the end of the room, add current coordinates to array
            coordinates.append((self.x, self.y))
            # if current y+1 and x is empty,then can move there;y axis down
            while self.area[self.y + 1][self.x] != "*":
                self.moveD(self.x, self.y)
                self.y += 1
                self.output_room()
            coordinates.append((self.x, self.y))
            while self.area[self.y][self.x - 1] != "*":
                self.moveL(self.x, self.y)
                self.x -= 1
                self.output_room()
            coordinates.append((self.x, self.y))
            while self.area[self.y - 1][self.x] != "*":
                self.moveU(self.x, self.y)
                self.y -= 1
                self.output_room()
            coordinates.append((self.x, self.y))
            # if first coordinates equal last then end program
            if coordinates[0] == coordinates[-1]:
                break
        # update self value of class to use in get distance
        self.endCoordinates = coordinates

    def get_distance(self):
        distance = 0.0
        for ind, i in enumerate(self.endCoordinates):
            if ind != len(self.endCoordinates) - 1:
                firstCoord = i
                secondCoord = self.endCoordinates[ind + 1]
                distance += sqrt((secondCoord[1] - firstCoord[1]) ** 2 + (secondCoord[0] - firstCoord[0]) ** 2)
            else:
                distance += sqrt(
                    (self.endCoordinates[0][1] - firstCoord[1]) ** 2 + (self.endCoordinates[0][0] - firstCoord[0]) ** 2)
        return distance


roomSize = int(input("Input value for the size of the room(atleast 4): "))
if roomSize < 4:
    print("Wrong")
    quit()
for i in range(10):
    room = room_creation(roomSize)
    room.create_room(roomSize - 1)
    # room.output_room()
    room.create_maze_pillar()
    room.create_maze_pillar()
    room.output_room()
dum = Dummy(room.room_array())
dum.update()
# print(dum.get_distance())
