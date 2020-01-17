from util.estado_equipo_pesado import EstadoEquipoPesado

class DetectorCiclo:
    def __init__(self):
        pass

    def es_ciclo(self, registros):
        # TODO: Implementar el algoritmo para detección de ciclos, la salida de la función es:
        # es_ciclo
        # estado_equipo_pesado
        estado_equipo_pesado = EstadoEquipoPesado.FUNCIONANDO
        es_un_ciclo = False
        return (es_un_ciclo, estado_equipo_pesado)