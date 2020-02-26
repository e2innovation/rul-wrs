from acceso_configuracion import AccesoConfiguracion
from acceso_datos.acceso_datos import AccesoDatos
from acceso_datos.cliente_base_datos import ClienteBaseDatos
from orquestador.orquestador import Orquestador

class ObtenerOrquestador:
    def __init__(self, archivo_configuracion):
        self.acceso_configuracion = AccesoConfiguracion(archivo_configuracion)

    @staticmethod
    def __obtener_cliente_base_datos(acceso_configuracion):
        configuracion = acceso_configuracion.obtener_configuracion("base_datos")
        db_cliente = ClienteBaseDatos(
                configuracion["driver"],
                configuracion["servidor"],
                configuracion["base_datos"],
                configuracion["usuario"],
                configuracion["contrasena"]
            )
        return AccesoDatos(db_cliente)

    @staticmethod
    def __obtener_preprocesador(acceso_configuracion):
        return None

    @staticmethod
    def __obtener_detector_ciclos(acceso_configuracion):
        return None

    @staticmethod
    def __obtener_clasificador(acceso_configuracion):
        return None

    @staticmethod
    def __obtener_predictor(acceso_configuracion):
        return None

    @staticmethod
    def obtener_orquestador(archivo_configuracion):
        acceso_configuracion = AccesoConfiguracion(archivo_configuracion)
        return Orquestador(
            ObtenerOrquestador.__obtener_cliente_base_datos(acceso_configuracion),
            ObtenerOrquestador.__obtener_detector_ciclos(acceso_configuracion),
            ObtenerOrquestador.__obtener_preprocesador(acceso_configuracion),
            ObtenerOrquestador.__obtener_clasificador(acceso_configuracion),
            ObtenerOrquestador.__obtener_predictor(acceso_configuracion)
        )