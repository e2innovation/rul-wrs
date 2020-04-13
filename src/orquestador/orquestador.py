from src.util.estado_equipo_pesado import EstadoEquipoPesado

class Orquestador:
    def __init__(self, acceso_datos, detector_ciclos, preprocesador, clasificador, predictor):
        self.acceso_datos = acceso_datos
        self.detector_ciclos = detector_ciclos
        self.preprocesador = preprocesador
        self.clasificador = clasificador
        self.predictor = predictor

    def monitorear(self):
        print('Obteniendo equipos')
        equipos_pesados = self.acceso_datos.seleccionar_equipos_pesados_activos()
        print(equipos_pesados)
        for equipo_pesado in equipos_pesados:
            registros = self.acceso_datos.seleccionar_registros_entrada(equipo_pesado)
            ciclos = self.detector_ciclos.detectar_ciclos(registros)
            for ciclo in ciclos:
                self.acceso_datos.guardar_ciclo(ciclo)
            