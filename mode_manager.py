from mode_move import Mode_move
from secret import Start 
from color import Color_handler as ch

dead = [0, 0, 0]

class State_manager:
    def __init__(self, sense, col):
        self.sense = sense
        self.col = col
        self.events = []
        self.mode = "Home"
        self.random = False 
        self.grid = []
        self.move_mode = Mode_move(self.sense, col)
        self.index = 0
        self.home_bl = False

    def add_event(self, event):
        self.events.append(event)
        self.event_checker(event)
    
    def event_checker(self, event ):
            event_tp = (event.direction, event.action) 
            if self.mode != "Draw":
                self.move_mode.thread_on = False

            if self.mode != "Prebuild":
                self.index = 0
                
            if event_tp == ("middle", "held") or self.home_bl:
                self.home(event_tp)

            else:
                match self.mode :
                    case "Home" | "Paused" :
                        match event_tp:
                            case ("middle", "released"):
                                self.mode = "Running"
                                print(self.mode)
                
                            case ("right", "released"):
                                self.mode = "Draw"
                                print(self.mode)
                                self.move_mode.thread_on = True
                                
                            case ("left", "released"):
                                print("found Easteregg")
                                Start(self.sense)

                            case ("up", "released"):
                                self.mode = "Prebuild"
                                self.do_shape()
                                print(self.mode)
                           
                    case "Draw":
                        self.move_mode.move(event_tp) 

                    case "Running":
                        if event_tp == ("middle", "released"):
                            self.mode = "Paused"
                            print(self.mode)

                    case "Prebuild":
                        if event_tp == ("middle", "released"):
                            self.mode = "Running"
                            print(self.mode)
                            
                        if event_tp == ("right", "released"):
                            self.index += 1

                        if event_tp == ("left", "released"):
                            self.index -=1

                        if self.index == 4:
                            self.index = 0
                        if self.index == -1:
                            self.index = 3
                        self.do_shape()


    def orientation(self, ori):
        if 170 < ori["roll"] < 190 or 170 < ori["pitch"] < 190 :
            if self.mode != "Home":
                print("reseted")
                self.mode = "Home"
            return True

        return False

    def acceleration(self, acc):
        for axis in acc:
            if acc[axis] >= abs(3):
                self.random = True

    def home(self, event_tp):
        self.home_bl = True
        if event_tp ==  ("middle", "released"):
            print(self.mode)
            self.home_bl = False
        self.mode = "Home"
        self.events = []

    def do_shape(self):
        mod_shap = [dead if j != 1 else ch.col(self.col)  for j in self.shapes(self.index)]
        self.sense.set_pixels(mod_shap)



    def shapes(self,index):
        ds = [[
                0, 1, 0, 0, 0, 0, 0, 0,
                0, 0, 1, 0, 0, 0, 0, 0,
                1, 1, 1, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0
                ],
               [
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 1, 1, 0,
                0, 0, 1, 1, 0, 1, 1, 0,
                0, 0, 1, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 1, 1, 0, 0,
                0, 1, 1, 0, 1, 1, 0, 0,
                0, 1, 1, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0
                ],

               [
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 1, 1, 0, 0, 0,
                0, 0, 1, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 1, 0, 0,
                0, 0, 0, 1, 1, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0
                ],
              [
                0, 0, 1, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 1, 1, 1, 1, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 1, 1, 1, 1, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 1, 0, 0
                ],
                

              ]
        return ds[index]
if __name__ == "__main__":
    State_manger()
