import copy
import json

class UtilDatos:
    @staticmethod
    def convertir_campo_json_a_objeto(objeto, campo):
        nuevo_objeto = copy.deepcopy(objeto)
        nuevo_objeto[campo] = json.loads(objeto[campo])
        return nuevo_objeto
