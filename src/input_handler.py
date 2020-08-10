from src.exceptions import StopPlayerException

def handle(inp):
    
    if inp == "":
        pass    
    elif inp == "quit":
        raise StopPlayerException
    else:
        print(inp)
