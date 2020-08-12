from mpyg321.mpyg321 import MPyg321Player

class Song:
    def __init__(self, id, name, playlist):
        self.location = id
        self.name = name
        self.playlist = playlist

class AudioPlayer:
    def __init__(self):
        self.player = MPyg321Player()
        self.current_song = None
        self.isPlaying = False

    def play(self, song: Song):
        self.player.play_song(f'./data/{song.id}.mp3')
        self.current_song = song
        self.isPlaying = True

    def pause(self):
        self.player.pause()
        self.isPlaying = False

    def resume(self):
        self.player.resume()
        self.isPlaying = True

    def stop(self):
        self.player.stop()
        self.isPlaying = False

