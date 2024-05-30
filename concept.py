from senese_hat import sense
col = dead

def place_bit(pos):
	if sense.get_pixel(pos) != dead:
		sense.set_pixel(pos[0],pos[1], rC())
	else:
		sense.set_pixel(pos[0],pos[1], dead)
def blinck():
	global col
	pos = self.cr_pos
	if self.mode = "Moving":
		while True:
			col = sense.get_pixel(pos)
			time.sleep(.5)
			sense.set_pixel(pos, dead)
			time.sleep(.5)
			sense.set_pixel(pos, col)
	
	


def Joy_stick():
    while True:
	event = sense.jostick.wait_for_event()
	if self.mode == "Moving":
		blink_thread.running = True
		if event.action == "released":
			if event.direction == "up":
	                    current_position = move("up", current_position)
       	        	elif event.direction == "down":
        	            current_position = move("down", current_position)
                	elif event.direction == "left":
	                    current_position = move("left", current_position)
        	        elif event.direction == "right":
                    	current_position = move("right", current_position)
	                elif event.direction == "middle":
        	            place_bit(current_pos)
	else:
		blink_thread.running(False)
def reset():
	global modeManager
	modeManager = None
	modeManager = ModeManager()
	
	


blinck_thread = threading.Thread(target=blinck)
blinck_thread.start()
joy_stick_thread = threading.Thread(target=Joy_stick)
joy_stick_thread.start()

while True:
	#code here
	if 
