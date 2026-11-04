class Camera:
    def take_photo(self):
        print("Taking photo")


class MusicPlayer:
    def play_music(self):
        print("Playing music")


class Smartphone(Camera, MusicPlayer):
    def calling(self):
        print("Making a call")


s1 = Smartphone()

s1.take_photo()
s1.play_music()
s1.calling()