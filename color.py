import sys
import random
	
class Color_handler():
	def col(color):
	    if color != None:
	        if color == "random":
	            return Color_handler.rC()
	        return color
	
	
	
	    col_dic = {"red" : [255, 0, 0],
	               "green" : [0, 255, 0],
	               "blue" : [0, 0, 255]}
	    syslen = len(sys.argv)
	
	    if  syslen == 2:
	        color = col_dic[sys.argv[1]]
	
	    elif syslen == 4:
	        color = [int(i) for i in sys.argv[1:]] 
	
	    else:
	        color = "random" 
	
	    return color
	 
	                
	def rC():
	    return [random.randint(1,255) for i in range(3)]
