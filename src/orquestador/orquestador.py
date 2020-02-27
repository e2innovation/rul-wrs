from util.estado_equipo_pesado import EstadoEquipoPesado

class Orquestador:
    def __init__(self, acceso_datos, detector_ciclos, preprocesador, clasificador, predictor):
        self.acceso_datos = acceso_datos
        self.detector_ciclos = detector_ciclos
        self.preprocesador = preprocesador
        self.clasificador = clasificador
        self.predictor = predictor

    def monitorear(self):
        equipos_pesados = self.acceso_datos.seleccionar_equipos_pesados()
        for equipo_pesado in equipos_pesados:
            registros = self.acceso_datos.seleccionar_registro_entrada(equipo_pesado)
            (es_ciclo, estado_equipo_pesado) = self.detector_ciclos.es_ciclo(registros)
            if equipo_pesado["ESTADO"] != estado_equipo_pesado:
                self.acceso_datos.cambiar_estado_equipo_pesado(equipo_pesado, estado_equipo_pesado)
            
            if es_ciclo :
                
                self.acceso_datos.crear_ciclo(equipo_pesado, registros)
                
            ciclos = self.acceso_datos.obtener_ciclos_no_finalizados(equipo_pesado)
            for ciclo in ciclos:
                caracteristicas = self.preprocesador.obtener_caracteristicas(registros)
                self.acceso_datos.guardar_caracteristicas(ciclo, caracteristicas)
            