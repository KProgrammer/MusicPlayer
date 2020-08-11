import src.exceptions as exceptions
from src.audio_downloader import AudioDownloader
from src.json_handler import JsonHandler
import src.storage as storage
from src.m_logging import Logger

import os

logger = Logger()

def download(params):    
    if storage.data["current_playlist"] == "":
        logger.log("Go to a playlist first", color=logger.color.red, effect=logger.effect.bold_effect)
        return

    jh = JsonHandler()
    data = jh.readFile()    

    def clbck(id):        
        # for playlist_data in data["playlists"].values():
        #     for song in playlist_data["songs"]:
        #         if song["id"] == id:                    
        #             return False         
        # return True            
        for f in os.listdir('./data'):
            if f[:-4] == id:
                return False
        return True                

    def success_hook(response):
        logger.log(f"Successfully downloaded {params[1]} in {storage.data['current_playlist']}", color=logger.color.green, effect=logger.effect.bold_effect)

    def downloading_hook(downloaded_bytes, total_bytes, elapsed, eta, speed):
        print(f"{logger.formattedText(downloaded_bytes *100/total_bytes, color=logger.color.yellow)}% completed")       
        
    def error_hook(response):
        logger.log("An error occured during downloading", color=logger.color.red)
    ad = AudioDownloader(downloading_hook, error_hook, success_hook)    
    data["playlists"][storage.data["current_playlist"]]["songs"].append({"id": ad.download_audio(params[0], clbck), "name": params[1]})
    jh.writeFile(data)

def make_playlist(params):    
    jh = JsonHandler()
    data = jh.readFile()
    for playlist in data["playlists"].keys():
        if playlist == params[0]:
            logger.log("A Playlist by that name already exists", color=logger.color.red, effect=logger.effect.bold_effect)            
            return
    data["playlists"][params[0]] = {"songs": []}
    jh.writeFile(data)
    logger.log("Made Playlist Successfully", color=logger.color.green)
    # storage.data["prompt"] = f"{params[0]}> "
    # storage.data["current_playlist"] = params[0]
    
def remove_playlist(params):
    jh = JsonHandler()
    data = jh.readFile()
    if params[0] not in data['playlists'].keys():
        logger.log('That playlist does not exist', color=logger.color.red, effect=logger.effect.bold_effect)
        return
    del data['playlists'][params[0]]
    jh.writeFile(data)
    logger.log("Playlist removed successfully", color=logger.color.yellow, effect=logger.effect.bold_effect)     

def view_playlists():
    jh = JsonHandler()
    data = jh.readFile()     
    print('\n'.join(data['playlists'].keys()))

def move_to_playlist(params):
    jh = JsonHandler()
    data = jh.readFile()
    if params[0] not in data['playlists'].keys():
        logger.log('That playlist does not exist', color=logger.color.red, effect=logger.effect.bold_effect)
        return
    storage.data["current_playlist"]=params[0]   

def view_songs():
    jh = JsonHandler()
    data = jh.readFile()
    if storage.data["current_playlist"] == "":
        logger.log("Go to a playlist first", color=logger.color.red, effect=logger.effect.bold_effect)
        return

    songs = [x["name"] for x in data['playlists'][storage.data["current_playlist"]]['songs']]

    print('\n'.join(songs))           

def nothing():
    pass

def quit():
    raise exceptions.StopPlayerException
    