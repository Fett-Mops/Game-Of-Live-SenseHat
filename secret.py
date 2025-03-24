import time
import os
import vlc

class Start:
    def __init__(self, sense, vid):
        self.sense = sense
        self.vid = vid


        self.run()

    def run(self):
        i = 0
        if vid == "apple":
            path = os.path.join(os.getcwd(),"frames", "Secret.mp4")
        else:
            path = os.path.join(os.getcwd(),"frames", "Rickr.mp4")

        
        instance = vlc.Instance()
        media = instance.media_new()
        player = instance.media_player_new()
        player.set_media(media)
        player.play()

        while i <= len(os.listdir(os.path.join("frames", vid))) -1:
            self.sense.load_image(osl.path.join("frames", vid ,"frame{}.jpg".format(i)))
            time.sleep(1/24)
            i += 1
        player.stop()
