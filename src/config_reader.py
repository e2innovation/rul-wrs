import json

class ConfigReader:
    def __init__(self, path):
        self.data = {}
        with open(path) as json_data_file:
            self.data = json.load(json_data_file)

    def get_value(self, key):
        return self.data[key]
