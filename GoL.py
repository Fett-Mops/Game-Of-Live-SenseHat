#!usr/bin/python3
from sense_hat import SenseHat
from signal import pause
import random

import time
from mode_manager import State_manager
from color import Color_handler as Ch 

sense = SenseHat()
sense.set_imu_config(True, False, True)

col = Ch.col(None)
row = column = 8
dead = [0,0,0]

clear = [dead for _ in range(64)]
board = []
color = None

   

def place(board, rand=False):
    for i in range(row):
        for j in range(column):
            if (i,j) in board:

                sense.set_pixel(i,j,Ch.col(col))
            elif rand and bool(random.getrandbits(1)):
                sense.set_pixel(i, j, Ch.col(col))
    board = []
   
def inRange(i,j,k)->bool:
        x = int(k[0]) + i
        y = int(k[1]) + j
        if - 1 < x < column and  - 1 < y < row:
            return True
        return False
    
    
def getNeighbour():
    newBoard = []
    
    for i in range(row):
        for j in range(column):
            neighbours = 0
            for k in [-1,0,1]:  
                for m in [-1, 0, 1]:
                    if m != 0 or k != 0:
                        if inRange(i, j, (k, m)):
                            if sense.get_pixel(i+k, j+m) != dead:
                                neighbours += 1
                            
            var = logic(i,j,neighbours)
            newBoard.append(var)
    return newBoard
                            

def logic(i, j, neighbours):
        #? Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        #? Any live cell with two or three live neighbors lives on to the next generation.
        #? Any live cell with more than three live neighbors dies, as if by overpopulation.
        #? Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
      
    if sense.get_pixel(i,j) != dead: 
        if neighbours == 2 or neighbours == 3: 
            return (i, j)

        elif neighbours > 3: 
            pass
    else: 
        if neighbours == 3:
            return (i, j)
                            




sense.set_pixels(clear)
state_manager = State_manager(sense, col)


while True:
    if state_manager.random:
        sense.set_pixels(clear)
        place(board, True)
        state_manager.random = False

    for event in sense.stick.get_events():
        state_manager.addEvent(event)

    if state_manager.orientation(sense.get_orientation()):
        state_manager = None
        state_manager = State_manager(sense, col)
        sense.set_pixels(clear)

    state_manager.acceleration(sense.get_accelerometer_raw())

    if state_manager.mode == "Running":
        board = getNeighbour()
        time.sleep(.3)
        sense.set_pixels(clear)
        place(board)
        print("running")
 



