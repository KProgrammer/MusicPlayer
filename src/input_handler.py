from src.exceptions import StopPlayerException
from src.command import Command
import src.functions as functions
from src.m_logging import Logger

logger = Logger()

commands = [
    Command(["", "\t"], 0, functions.nothing),
    Command(["q", "quit"], 0, functions.quit),
    Command(["d", "download"], 2, functions.download),
    Command(["mp", "make_playlist"], 1, functions.make_playlist),
    Command(["rp", "remove_playlist"], 1, functions.remove_playlist),    
    Command(["->", '=>', 'mt', 'move_to'], 1, functions.move_to_playlist),
    Command(["pl", "playlists"], 0, functions.view_playlists),
    Command(["s", "so"], 0, functions.view_songs)
]

def getCommandData(inp: str)->dict:
    split_inp = inp.split()
    if inp == "":
        return { "command": "", "params": [] }
    return { "command": split_inp[0], "params": split_inp[1:] }

def handle(inp):    
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
