import src.exceptions as exceptions
from src.audio_downloader import AudioDownloader
from src.json_handler import JsonHandler
import src.storage as storage

import os


def download(params):    
    if storage.data["current_playlist"] == "":
        print("Go to a playlist first")
        return

    jh = JsonHandler()
    data = jh.readFile()    

    def clbck(id):        
        for playlist_data in data["playlists"].values():
            for song in playlist_data["songs"]:
                if song["id"] == id:                    
                    return False         
        return True    

    def success_hook(response):
        print("success")

    def downloading_hook(downloaded_bytes, total_bytes, elapsed, eta, speed):
        print(downloaded_bytes * 100/total_bytes)        
    def null_hook(response):
        pass
    ad = AudioDownloader(downloading_hook, null_hook, success_hook)    
    data["playlists"][storage.data["current_playlist"]]["songs"].append({"id": ad.download_audio(params[0], clbck), "name": params[1]})
    jh.writeFile(data)

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

def view_playlists():
    jh = JsonHandler()
    data = jh.readFile() 
    print('\n'.join(data['playlists'].keys()))

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
    