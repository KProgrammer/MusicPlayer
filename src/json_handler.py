import json

class JsonHandler:    
    def __init__(self, file='/home/kprogrammer/Desktop/PythonProjects/MusicPlayer/config.json'):
        self.file = file

    def readFile(self):
        with open(self.file) as f:
            data = json.load(f)
        return data

    def writeFile(self, dic):
        with open(self.file, 'w') as json_file:
            json.dump(dic, json_file)
         