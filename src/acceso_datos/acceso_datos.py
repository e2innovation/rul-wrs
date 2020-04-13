from util.estado_ciclo import EstadoCiclo
from util.estado_equipo_pesado import EstadoEquipoPesado
from acceso_datos.util_acceso_datos import UtilDatos
from util.formatea_entrada import FormateaEntrada
import json

class AccesoDatos:
    def __init__(self, bd_cliente):
        self.bd_cliente = bd_cliente

    @staticmethod
    def cambiar_a_enum_estado(equipo_pesado):
        equipo_pesado["ESTADO"] = EstadoEquipoPesado.of(equipo_pesado["ESTADO"])
        return equipo_pesado

    def seleccionar_equipos_pesados_activos(self):
        resultado = self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.SELECCIONAR_EQUIPO_PESADO")
        equipos_pesados = resultado[0]
        return [AccesoDatos.cambiar_a_enum_estado(equipo_pesado) for equipo_pesado in equipos_pesados if equipo_pesado["ESTADO"] != EstadoEquipoPesado.BAJA.value]

    def cambiar_estado_equipo_pesado(self, equipo_pesado, estado):
        self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.CAMBIAR_ESTADO_EQUIPO_PESADO", [equipo_pesado["EQUIPO_PESADO_ID"], estado.value])

    def seleccionar_registros_entrada(self, equipo_pesado):
<<<<<<< HEAD
        resultado = self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.SELECCIONAR_REGISTRO_ENTRADA", [equipo_pesado["EQUIPO_PESADO_ID"]])
        registros_entrada = resultado[0]
        registros = [UtilDatos.convertir_campo_json_a_objeto(registro_entrada, "REGISTRO") for registro_entrada in registros_entrada]
        dataframe = FormateaEntrada.registros_a_dataframe(registros)
        FormateaEntrada.generar_campos_inv(dataframe)
        campos = [
            'VEL_REF_HOIST',
            'VEL_REFERENCIA_CROWD',
            'DIPEER_TRIP',
            'TORQUE_HOIST_INV',
            'CORRIENTE_IW_HOIST_INV',
            'POTENCIA_KW_HOIST',
            'VELOCIDAD_HOIST_INV',
            'LONGITUD_CABLE_HOIST_INV',
            'EXTENSION_CROWD',
            'ANGULO_SWING',
=======
<<<<<<< Updated upstream
        resultado = self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.SELECCIONAR_REGISTRO_ENTRADA", [equipo_pesado["EQUIPO_PESADO_ID"]])
        registros_entrada = resultado[0]
        registros = [UtilDatos.convertir_campo_json_a_objeto(registro_entrada, "REGISTRO") for registro_entrada in registros_entrada]
=======
        resultado = self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.SELECCIONAR_REGISTRO_ENTRADA", [equipo_pesado['EQUIPO_PESADO_ID']])
        registros = resultado[0]
        if len(registros) == 0:
            return pd.DataFrame()
>>>>>>> Stashed changes
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
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
            'DIG_MODE'
        ]
        FormateaEntrada.normalizar_campos(dataframe, campos)
        return dataframe

<<<<<<< Updated upstream
    def crear_ciclo(self, equipo_pesado, registros):
        if len(registros) > 0:
            inicio = registros[0]["FECHA_HORA"]
            fin = registros[len(registros) - 1]["FECHA_HORA"]
            resultado = self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.CREAR_CICLO", [
                equipo_pesado["EQUIPO_PESADO_ID"],
                inicio,
                fin,
                EstadoCiclo.CREADO.value
            ])
            nuevo_ciclo = resultado[0][0]
            for registro in registros:
                registro_serializado = json.dumps(registro)
                self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.GUARDAR_CICLO_DETALLE", [
                    nuevo_ciclo.CICLO_ID,
                    registro_serializado
                ])

    def guardar_ciclo_caracteristicas(self, ciclo, vectores_caracteristicas):
        for vectores_caracteristicas in vectores_caracteristicas:
            caracteristicas_serializadas = json.dumps(vectores_caracteristicas)
            self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.GUARDAR_CICLO_CARACTERISTICAS", [
                ciclo["CICLO_ID"],
                caracteristicas_serializadas
            ])

        



=======
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
>>>>>>> Stashed changes
