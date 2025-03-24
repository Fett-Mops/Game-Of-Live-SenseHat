import time
import threading
from color import Color_handler as Ch

class Mode_move():
    def __init__(self, sense, col):
        self.cr_pos = [0, 0]
        self.sense = sense
        self.col = col
        self.active = False
        self.thread_on = False
        self.blinck_th = threading.Thread(target=self.blincking, daemon = True)
        self.blinck_th.start()
        self.dead = [0,0,0]
        self.old_col =[0,0,0] 
        self.thread_stopper = False
        self.first = True
        self.rand_col = [255,0,0]

    def move(self, event):
        match event:
            case ("up","released"):
                self.in_range(x = -1) 
            case ("left", "released"):
                self.in_range(y = -1) 

            case ("down","released"):
                self.in_range(x = 1) 
                
            case ("right", "released"):
                self.in_range(y = 1) 
            case ("middle", "released"):
                if self.old_col == self.dead:
                    self.old_col = Ch.col(self.col)

                    self.sense.set_pixel(self.cr_pos[0], self.cr_pos[1], self.old_col)
                else:
                    self.old_col = self.dead
                    self.sense.set_pixel(self.cr_pos[0], self.cr_pos[1], self.dead)
                    

    def in_range(self, x = 0, y = 0):
        if -1 < self.cr_pos[0] + y < 8:
            if -1 < self.cr_pos[1] + x < 8:
                self.thread_stopper = True
                self.sense.set_pixel(self.cr_pos[0], self.cr_pos[1], self.old_col)
                self.cr_pos = [self.cr_pos[0] + y, self.cr_pos[1] + x]
                self.old_col = self.sense.get_pixel(self.cr_pos[0], self.cr_pos[1])
                self.thread_stopper = False

    def blincking(self):
        while True:
            if self.thread_on:
                if self.thread_stopper is False:
                    self.sense.set_pixel(self.cr_pos[0], self.cr_pos[1], self.rand_col)
                    time.sleep(.3)
                    self.sense.set_pixel(self.cr_pos[0], self.cr_pos[1], self.old_col)

            time.sleep(.3)
    
