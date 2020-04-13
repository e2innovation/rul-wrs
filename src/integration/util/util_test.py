import pandas as pd
import numpy as np

class UtilTest:
    @staticmethod
    def insertar_archivo_csv_en_tabla(path, conexion, nombre_tabla):
        df = pd.read_csv(path, sep=',' , engine='python')
        columns = ','.join( [f"[{column}]" for column in df.columns])
        marcas = ','.join(['?'] * len(df.columns))
        cursor = conexion.cursor()
        for row in df.itertuples(index=False):

            sql = f"INSERT INTO {nombre_tabla}({columns}) VALUES ({marcas})"
            data = tuple(row)
            cursor.execute(sql, data)
            conexion.commit()

    @staticmethod
    def insertar_equipo_pesado_prueba(conexion, nombre_equipo):
        parametros = [
            nombre_equipo,
            'PALA',
            'PALA DE PRUEBA',
            'HABILITADO',
            '-'
        ]
        cursor = conexion.cursor()
        cursor.execute(f"{{CALL dbo.GUARDAR_EQUIPO_PESADO(?, ?, ?, ?, ?)}}", parametros)
        cursor.commit()
    
    @staticmethod
    def obtener_ciclos_por_equipo(bd_cliente, nombre_equipo):
        parametros = [nombre_equipo]
        resultados = bd_cliente.ejecutar_procedimiento_almacenado('dbo.INFORMACION_CICLOS_POR_EQUIPO', parametros)
        print("***************************************************************")
        print(resultados)
        print(parametros)
        return resultados[0][0]['CANTIDAD_CICLOS']

    @staticmethod
    def eliminar_data_prueba(conexion, nombre_equipo):
        cursor = conexion.cursor()
        sql = """
        DECLARE @EQUIPO_PESADO_ID AS VARCHAR(256)
        SET @EQUIPO_PESADO_ID = ?
        DELETE FROM dbo.IOT_GATEWAY WHERE MACHINE_IDENTIFIER = @EQUIPO_PESADO_ID
        DELETE FROM dbo.REGISTRO_ENTRADA WHERE EQUIPO_PESADO_ID = @EQUIPO_PESADO_ID
        DELETE FROM dbo.CICLO_DETALLE WHERE CICLO_ID IN (
            SELECT CICLO_ID
            FROM dbo.CICLO
            WHERE EQUIPO_PESADO_ID = @EQUIPO_PESADO_ID
        )
        DELETE FROM dbo.CICLO WHERE EQUIPO_PESADO_ID = @EQUIPO_PESADO_ID
        DELETE FROM dbo.EQUIPO_PESADO WHERE EQUIPO_PESADO_ID = @EQUIPO_PESADO_ID
        """
        
        cursor.execute(sql, [nombre_equipo])
        conexion.commit()