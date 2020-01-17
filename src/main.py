from acceso_configuracion import AccesoConfiguracion
from acceso_datos.acceso_datos import AccesoDatos
from acceso_datos.cliente_base_datos import ClienteBaseDatos

def main(arg) : 
    acceso_configuracion = AccesoConfiguracion("../config.json")
    configuracion = acceso_configuracion.obtener_configuracion("base_datos")
    db_cliente = ClienteBaseDatos(
            configuracion["driver"],
            configuracion["servidor"],
            configuracion["base_datos"],
            configuracion["usuario"],
            configuracion["contrasena"]
        )
    acceso_datos = AccesoDatos(db_cliente)
    print(acceso_datos.seleccionar_equipos_pesados())

main(0)
