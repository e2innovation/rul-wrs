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
            'DIG_MODE'
        ]
        FormateaEntrada.normalizar_campos(dataframe, campos)
        return dataframe

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

        



