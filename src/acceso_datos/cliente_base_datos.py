import pyodbc

class ClienteBaseDatos:
    def __init__(self, driver, servidor, base_datos, usuario, contraseña):
        self.conexion = pyodbc.connect(
            f"DRIVER={{{driver}}};SERVER={servidor};DATABASE={base_datos};UID={usuario};PWD={contraseña}"
        )

    def ejecutar_procedimiento_almacenado(self, procedimiento_almacenado, parametros = []):
        cursor = self.conexion.cursor()
        marcas_parametros = "" if len(parametros) == 0 else f" ({','.join(['?'] * len(parametros))})"
        cursor.execute(f"{{CALL {procedimiento_almacenado}{marcas_parametros}}}", parametros)
        if not cursor.description is None:
            columnas = [columna[0] for columna in cursor.description]
            resultados = []
            filas = cursor.fetchall()
            while filas:
                resultado = []
                for fila in filas:
                    resultado.append(dict(zip(columnas, fila)))
                resultados.append(resultado)
                if cursor.nextset():
                    filas = cursor.fetchall()
                else:
                    filas = None
            cursor.close()
            return resultados if len(resultados) > 0 else [[]] # Si no trae ningun resultado al menos se devuelve una sola tabla vacia
        return None