import vlc
import time
instance = vlc.Instance()
media = instance.media_new("/Secret.mp4")
player = instance.media_player_new()
player.set_media(media)
player.play()
time.sleep(10)
player.stop()
