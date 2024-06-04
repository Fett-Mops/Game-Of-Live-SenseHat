import time
import os
import vlc

class Start:
    def __init__(self, sense):
        self.sense = sense

        self.run()

    def run(self):
        i = 0
        
        instance = vlc.Instance()
        media = instance.media_new(os.path.join(os.getcwd(),"Secret.mp4"))
        player = instance.media_player_new()
        player.set_media(media)
        player.play()

        while i <= len(os.listdir("frames")):
            print("frames/frame{}.jpg".format(i))
            self.sense.load_image("frames/frame{}.jpg".format(i))
            time.sleep(1/24)
            i += 1
        player.stop()
