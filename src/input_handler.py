from src.exceptions import StopPlayerException
from src.command import Command
import src.functions as functions

commands = [
    Command(["", "\t"], 0, functions.nothing),
    Command(["q", "quit"], 0, functions.quit),
    Command(["d", "download"], 2, functions.download),
    Command(["mp", "make_playlist"], 1, functions.make_playlist)    
]

def getCommandData(inp: str)->dict:
    split_inp = inp.split()
    if inp == "":
        return { "command": "", "params": [] }
    return { "command": split_inp[0], "params": split_inp[1:] }

def handle(inp):    
    gcd = getCommandData(inp)
    for command in commands:
        if gcd["command"] in command.aliases and len(gcd["params"]) == command.params_no:
            command.run(gcd["params"])
            return 
    print("Command with enough params not found")    

    # if inp == "":
    #     pass    
    # elif inp == "quit":
    #     raise StopPlayerException
    # else:
    #     print(inp)
