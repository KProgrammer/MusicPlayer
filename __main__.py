from src.exceptions import StopPlayerException
from src.logging import Logger
import src.input_handler 

while(1):    
    try:
        inp = input("> ")        
        src.input_handler.handle(inp)            
    except KeyboardInterrupt:
        print("\nMusic Player Stopped")
        break        
    except StopPlayerException:
        print("Music Player Stopped")
        break