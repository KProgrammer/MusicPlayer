from src.exceptions import StopPlayerException
from src.command import Command
import src.functions as functions
from src.m_logging import Logger

logger = Logger()

commands = [
    Command(["", "\t"], 0, functions.nothing, "", {}),
    Command(["q", "quit"], 0, functions.quit, "Quits the program", {}),
    Command(["d", "download"], 2, functions.download, "Downloads audio from the youtube url and saves it with a name", {"url": "The youtube url from which audio gets downloaded", "name": "The name by which the audio will be recognized"}),
    Command(["mp", "make_playlist"], 1, functions.make_playlist, "Makes a playlist with a name", {"name": "The name of the new playlist"}),
    Command(["rp", "remove_playlist"], 1, functions.remove_playlist, "Deletes a playlist", {"name": "The playlist to delete"}),    
    Command(["->", '=>', 'mt', 'move_to'], 1, functions.move_to_playlist, "Move to playlist to download and play music", {"name": "The name of the playlist to move to"}),
    Command(["pl", "playlists"], 0, functions.view_playlists, "View the playlists created", {}),
    Command(["so", "songs"], 0, functions.view_songs, "View the songs in the current playlist", {}),
    Command(["play"], 1, functions.play_song, "Plays the song from the playlist", {"name": "Name of the song"}),
    # Command(["playp"], 0, functions.play_playlist, "Plays the current playlist in random order", {}),
    # Command(["p"], 0, functions.p, "Plays/Pauses the current song", {}),
    # Command(["s", "stop"], 0, functions.stop, "Stops the current song", {})
]

def getCommandData(inp: str)->dict:
    split_inp = inp.split()
    if inp == "":
        return { "command": "", "params": [] }
    return { "command": split_inp[0], "params": split_inp[1:] }

def handle(inp):
    if inp == 'help':        
        for command in commands:
            if command.aliases[0] != "":
                print(f"{'Command':{10}.{7}}: {logger.formattedText(' or '.join(command.aliases), color=logger.color.green)}\n{'Function':{10}.{8}}: {logger.formattedText(command.function, color=logger.color.yellow)}\n{'Parameters:' if command.params_no != 0 else ''}")
                for param in command.param_data:
                    print(f"{logger.formattedText(param, color=logger.color.cyan)}: {command.param_data[param]}")
                print()                    
    else:
        gcd = getCommandData(inp)
        for command in commands:
            if gcd["command"] in command.aliases:
                if len(gcd["params"]) == command.params_no:
                    command.run(gcd["params"])
                    return 
                else:
                    logger.log(f"Command takes {command.params_no} param{'' if command.params_no == 1 else 's'}", color=logger.color.red, effect=logger.effect.bold_effect)
                    return
        logger.log("Command not found", color=logger.color.red, effect=logger.effect.bold_effect)    
