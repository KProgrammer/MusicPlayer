class Command:
    def __init__(self, aliases, params_no, runner, function, param_data):
        self.aliases = aliases
        self.params_no = params_no
        self.runner = runner
        
        self.function = function
        self.param_data = param_data

    def run(self, params):
        if self.params_no != 0:
            self.runner(*params)
        else:
            self.runner()
    
        