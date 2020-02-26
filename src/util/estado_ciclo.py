from enum import Enum

class EstadoCiclo(Enum):
    CREADO = 'CREADO'
    CON_CARACTERISTICAS = 'CON_CARACTERISTICAS'
    CLASE_ASIGNADA = 'CLASE_ASIGNADA'
    PROCESADO_COMPLETO = 'PROCESADO_COMPLETO'

    @staticmethod
    def of(value):
        resultado = [estado for estado in EstadoCiclo if estado.value == value]
        return resultado[0]