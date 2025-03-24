import sys
import random
	
class Color_handler():
    def col(color):
        if color != None:
            if color == "random":
                return Color_handler.rC()
            return color
        
        col_dic = {"-r" : [255, 0, 0],
                   "-g" : [0, 255, 0],
                   "-b" : [0, 0, 255],
                   "-y" : [255, 255, 0],
                   "-p" : [160, 32, 240],
                   "-w" : [255, 255, 255],
                   "-o" : [255, 165, 0],
                   "-b" : [165, 42, 42],
                   "-rgb" : "random"}

        syslen = len(sys.argv)
	
        try:
            if  syslen == 4:
                try:
                    color = [int(i) for i in sys.argv[1:]] 
                except:
                    print("input error: expects only int")

            elif syslen == 2:
                try:
                    color = col_dic[sys.argv[1].lower()]
                except:
                    print("input error: expect value in {col_dic.keys()}, not {sys.argv[1]}")
        
            else:
                color = [128, 128,128]
        except:
            color = [128, 128,128]

        return color
	 
	                
    def rC():
        return [random.randint(1,255) for i in range(3)]
