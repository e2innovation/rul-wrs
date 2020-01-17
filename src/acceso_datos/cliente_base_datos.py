import pyodbc

class ClienteBaseDatos:
    def __init__(self, driver, servidor, base_datos, usuario, contraseña):
        self.coneccion = pyodbc.connect(
            f"DRIVER={{{driver}}};SERVER={servidor};DATABASE={base_datos};UID={usuario};PWD={contraseña}"
        )

    def ejecutar_procedimiento_almacenado(self, procedimiento_almacenado, parametros = []):
        cursor = self.coneccion.cursor()
        marcas_parametros = "" if len(parametros) == 0 else f" ({','.join(['?'] * len(parametros))})"
        cursor.execute(f"{{CALL {procedimiento_almacenado}{marcas_parametros}}}", parametros)
        resultado = []
        filas = cursor.fetchall()
        while filas:
            resultado.append(filas)
            if cursor.nextset():
                filas = cursor.fetchall()
            else:
                filas = None
        cursor.close()
        return resultado
        