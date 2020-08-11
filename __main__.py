from src.exceptions import StopPlayerException
import src.input_handler 
import src.functions as functions
import src.storage as storage

storage.initialize()

while(1):    
    try:
        inp = input(f"{storage.data['current_playlist']}> ")        
        src.input_handler.handle(inp)            
    except KeyboardInterrupt:
        print("\nMusic Player Stopped")
        break        
    except StopPlayerException:
        print("Music Player Stopped")
        break