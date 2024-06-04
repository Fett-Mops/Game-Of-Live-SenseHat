from mode_move import Mode_move

dead = [0, 0, 0]

class State_manager:
    def __init__(self, sense, col):
        self.events = []
        self.mode = "Home"
        self.random = False 
        self.grid = []
        self.move_mode = Mode_move(sense, col)
        self.index = 0
        self.home_bl = False

    def addEvent(self, event):
        self.events.append(event)
        self.eventChecker(event)
    
    def eventChecker(self, event ):
            event_tp = (event.direction, event.action) 
            if self.mode != "Draw":
                self.move_mode.active = False
            if event_tp == ("middle", "held") or self.home_bl:
                print("jjj")
                self.home(event_tp)
            else:
                match self.mode :
                    case "Home" | "Paused" :
                        match event_tp:
                            case ("middle", "released"):
                                self.mode = "Running"

                            case ("up", "released"):
                                self.mode = "Prebuild"
                
                            case ("right", "released"):
                                self.mode = "Draw"
                                self.move_mode.actve = True
                            case _: 
                                print(event_tp, "Not implemented")
                
                    case "Draw":
                        self.move_mode.move(event_tp) 
                
                    case "Prebuild":
                        pass

                    case "Running":
                        if event_tp == ("middle", "released"):
                            self.mode = "Paused"



    def orientation(self, ori):
        if 140 < ori["roll"] < 220:
                print("reseted")
                return True

        return False

    def acceleration(self, acc):
        for axis in acc:
            if acc[axis] >= abs(3):
                print("random")
                self.random = True
    def home(self, event_tp):
        self.home_bl = True
        if event_tp ==  ("middle", "released"):
            self.home_bl = False
        self.mode = "Home"
        self.events = []
        print("jjj")

    def initShapes():
        return {"glider" : [dead, dead, dead, dead, dead, dead, dead, dead,
                            dead, dead, dead, dead, dead, dead, dead, dead,
                            dead, dead, dead, dead, dead, dead, dead, dead,
                            dead, dead, dead, dead, dead, dead, dead, dead,
                            dead, dead, dead, dead, dead, dead, dead, dead,
                            dead, dead, dead, dead, dead, dead, dead, dead,
                            dead, dead, dead, dead, dead, dead, dead, dead,
                            dead, dead, dead, dead, dead, dead, dead, dead]}
if __name__ == "__main__":

    State_manger()
