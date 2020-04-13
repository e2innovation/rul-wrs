import json
import pandas as pd
from src.util.formatea_entrada import FormateaEntrada
from src.util.estado_equipo_pesado import EstadoEquipoPesado
from src.util.estado_ciclo import EstadoCiclo

class AccesoDatos:
    def __init__(self, bd_cliente):
        self.bd_cliente = bd_cliente

    def seleccionar_equipos_pesados_activos(self):
        resultado = self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.SELECCIONAR_EQUIPO_PESADO")
        equipos = resultado[0]
        return [equipo for equipo in equipos if EstadoEquipoPesado[equipo['ESTADO']] is EstadoEquipoPesado.HABILITADO]

    def seleccionar_registros_entrada(self, equipo_pesado):
        resultado = self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.SELECCIONAR_REGISTRO_ENTRADA", [equipo_pesado['EQUIPO_PESADO_ID']])
        registros = resultado[0]
        if len(registros) == 0:
            return pd.DataFrame()
        dataframe = FormateaEntrada.registros_a_dataframe(registros)
        FormateaEntrada.generar_campos_inv(dataframe)
        campos = [
            'HOIST_SPEED_REF',
            'CROWD_SPEED_REF',
            'DIPEER_TRIP',
            'HOIST_TORQUE_INV',
            'HOIST_IW_INV',
            'HOIST_KW',
            'HOIST_SPEED_INV',
            'HOIST_ROPE_LENGTH_INV',
            'CROWD_EXTENSION',
            'SWING_ANGLE',
            'DIG_MODE'
        ]
        FormateaEntrada.normalizar_campos(dataframe, campos)
        return dataframe

    def guardar_ciclo(self, ciclo):
        # 1. Crear ciclo 
        self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.CREAR_CICLO", [ciclo['EQUIPO_PESADO_ID'], EstadoCiclo.CREADO.value])
        resultado = self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.LEER_ULTIMO_CICLO", [])
        ciclo_creado = resultado[0][0]
        print(ciclo_creado)
        ciclo['CICLO_ID'] = ciclo_creado['CICLO_ID']

        # 2. Crear el detalle de ciclos
        self.crear_etapa_ciclo(ciclo, 'excavar')
        self.crear_etapa_ciclo(ciclo, 'transportar')
        self.crear_etapa_ciclo(ciclo, 'descargar')

        # 3. Eliminar registros que no forman parte de un ciclo, por ejemplo los que se quedaron en la etapa INICIO
        self.bd_cliente.ejecutar_procedimiento_almacenado('dbo.BORRAR_REGISTROS_FUERA_DE_CICLO', [
            ciclo_creado['EQUIPO_PESADO_ID'],
            ciclo_creado['CICLO_ID'],
            ciclo['fin'].item()
        ])

    def crear_etapa_ciclo(self, ciclo, etapa):
        for registroId in ciclo[etapa]:
            self.bd_cliente.ejecutar_procedimiento_almacenado('dbo.CREAR_CICLO_DETALLE', [
                ciclo['CICLO_ID'],
                etapa,
                registroId.item()
            ])
