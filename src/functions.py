import src.exceptions as exceptions
from src.audio_downloader import AudioDownloader
from src.json_handler import JsonHandler
import src.storage as storage

import os


def download(params):
    def success_hook(response):
        print("success")
    def null_hook(response):
        pass
    ad = AudioDownloader(null_hook, null_hook, success_hook)
    ad.download_audio(params[0], params[1])

def make_playlist(params):    
    jh = JsonHandler()
    data = jh.readFile()
    for playlist in data["playlists"].keys():
        if playlist == params[0]:
            print("A Playlist by that name already exists")
            return
    data["playlists"][params[0]] = {"songs": []}
    jh.writeFile(data)
    print("Made Playlist Successfully")
    # storage.data["prompt"] = f"{params[0]}> "
    # storage.data["current_playlist"] = params[0]
    
def remove_playlist(params):
    jh = JsonHandler()
    data = jh.readFile()
    if params[0] not in data['playlists'].keys():
        print('That playlist does not exist')
        return
    del data['playlists'][params[0]]
    jh.writeFile(data)
    print("Playlist removed successfully")       

def move_to_playlist(params):
    jh = JsonHandler()
    data = jh.readFile()
    if params[0] not in data['playlists'].keys():
        print('That playlist does not exist')
        return
    storage.data["current_playlist"]=params[0]        

def nothing():
    pass

def quit():
    raise exceptions.StopPlayerException
    