import sys
import os

from src.obtener_orquestador import ObtenerOrquestador

def main(arg):
    ruta_aplicacion = os.path.dirname(sys.executable)
    ruta_archivo_configuracion = os.path.join(ruta_aplicacion, "config.json")
    try:
        orquestador = ObtenerOrquestador.obtener_orquestador(ruta_archivo_configuracion)
        orquestador.monitorear()
    except Exception as ex:
        print(ex)

if __name__ == "__MAIN__":
    main(sys.argv)