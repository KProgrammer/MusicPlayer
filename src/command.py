class Command:
    def __init__(self, aliases, params, runner):
        self.aliases = aliases
        self.params = params
        self.runner = runner

    def run(self, params):
        self.runner(params)        

        