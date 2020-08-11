from src.exceptions import StopPlayerException
import src.input_handler 
import src.functions as functions
import src.storage as storage
from src.m_logging import Logger

storage.initialize()

logger = Logger()

while(1):    
    try:
        inp = input(f"{storage.data['current_playlist']}> ")        
        src.input_handler.handle(inp)            
    except KeyboardInterrupt:
        logger.log("\nMusic Player Stopped", color=logger.color.red, effect=logger.effect.bold_effect)
        break        
    except StopPlayerException:
        logger.log("Music Player Stopped", color=logger.color.red, effect=logger.effect.bold_effect)
        break