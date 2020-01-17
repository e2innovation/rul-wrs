import json

class AccesoConfiguracion:
    def __init__(self, ruta_archivo):
        self.configuracion = {}
        with open(ruta_archivo) as archivo_json:
            self.configuracion = json.load(archivo_json)

    def obtener_configuracion(self, seccion):
        return self.configuracion[seccion]
