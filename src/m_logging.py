class Logger:    

    """ Class to organize logs better using colors and formats """

    class color:
        """ Class which contains the ansi codes to each color so you can use it in Logger functions """

        black = 30
        red = 31
        green = 32
        yellow = 33
        blue = 34
        purple = 35
        cyan = 36
        white = 37

    class effect:        
        """ Class which contains the ansi codes to each effect so you can use it in Logger functions """

        no_effect = 0
        bold_effect = 1
        dim_effect = 2
        italic_effect = 3 
    
    def formattedText(self, text, color=37, effect=0, bg=40) -> str:
        """ returns a string which is formatted using ansi escape strings """
        return f"\033[{effect};{color};{bg+10}m{text}\033[00m"

    def log(self, *args, color=37, effect=0, bg=40, end='\n', sep=' '):
        """ prints text passed into args in a particular style"""


        for i in range(len(args)):
            print(self.formattedText(args[i], color=color, effect=effect, bg=bg), end='')
            if i != len(args) - 1:
                print(sep, end='')

        print(end, end='')    

    def printFormat(self, format, **kwargs):
        """ prints the format with the given parameters 
        
            Parameters
            ----------
            format: function which returns a string
                The kwargs given will be passed onto the format function
        
        """        

        print(format(**kwargs))    
