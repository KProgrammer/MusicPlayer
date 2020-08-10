
class Command:
    def __init__(self, aliases, params_no, runner):
        self.aliases = aliases
        self.params_no = params_no
        self.runner = runner

    def run(self, params):
        if self.params_no != 0:
            self.runner(params)
        else:
            self.runner()                    
