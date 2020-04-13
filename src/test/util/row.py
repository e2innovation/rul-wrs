"""
Esta clase nos sirve para mockear el resultado de pyodbc.row 
"""
class Row(object):
    def __init__(self, dict):
        self.__dict__ = dict

    def __iter__(self): # iterate over all keys
        for value in self.__dict__.values():
            yield value

    def __len__(self):
        return len(self.__dict__.values())