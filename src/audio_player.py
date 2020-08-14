from mpyg321.mpyg321 import MPyg321Player
import random

class MyPlayer(MPyg321Player):
    def __init__(self, after_music):
        self.after_music = after_music
        super().__init__()
    def onMusicEnd(self):
        self.after_music()

class Song:
    def __init__(self, id, name, playlist):
        self.id = id
        self.name = name
        self.playlist = playlist

class AudioPlayer:
    def __init__(self, playlist=None):
        if playlist:
            self.m_player = MyPlayer(self.nextSong)
            self.idx = 0
            self.playlist = playlist
            random.shuffle(self.playlist)
        else:
            self.m_player = MPyg321Player()
        self.current_song = None
        self.isPlaying = False

    def play(self, song: Song):
        self.m_player.play_song(f'/home/kprogrammer/Desktop/PythonProjects/MusicPlayer/data/{song.id}.mp3')
        self.current_song = song
        self.isPlaying = True

    def pause(self):
        self.m_player.pause()
        self.isPlaying = False

    def resume(self):
        self.m_player.resume()
        self.isPlaying = True

    def stop(self):
        self.m_player.stop()
        self.isPlaying = False

    def playPlaylist(self):        
        self.play(self.playlist[0])
        self.idx+=1

    def nextSong(self):
        if self.idx < len(self.playlist):
            self.play(self.playlist[self.idx])
            self.idx+=1
