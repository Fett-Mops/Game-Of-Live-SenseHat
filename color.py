import sys
import random
	
class Color_handler():
	def col(color):
	    if color != None:
	        if color == "random":
	            return Color_handler.rC()
	        return color
	
	
	yellow 🟨 purple 🟪 white ⬜ orange 🟧 brown 🟫
	    col_dic = {"red" : [255, 0, 0],
	               "green" : [0, 255, 0],
	               "blue" : [0, 0, 255],
		       "yellow" : [255, 255, 0],
		       "purple" : [160, 32, 240],
		       "white" : [255, 255, 255],
		       "orange" : [255, 165, 0],
		       "brown" : [165, 42, 42]}

	    #implement better error handeling
	    syslen = len(sys.argv)
	
	    if  syslen == 2:
	        color = col_dic[sys.argv[1].lower_case()]
	
	    elif syslen == 4:
	        color = [int(i) for i in sys.argv[1:]] 
	
	    else:
	        color = "random" 
	    return color
	 
	                
	def rC():
	    return [random.randint(1,255) for i in range(3)]
