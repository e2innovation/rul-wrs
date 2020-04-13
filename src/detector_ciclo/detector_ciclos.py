from src.util.etapa_ciclo import EtapaCiclo

class DetectorCiclos:
    def __init__(self, configuracion):
        self.umbral_cambio_velocidad_hoist = configuracion['umbral_cambio_velocidad_hoist']
<<<<<<< HEAD
        self.umbral_largo_cable = configuracion['umbral_largo_cable']
=======
        self.umbral_largo_cable_excavar = configuracion['umbral_largo_cable_excavar']
        self.umbral_largo_cable_transportar = configuracion['umbral_largo_cable_transportar']
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
        
    def detectar_ciclos(self, entradas_dataframe):
        entradas = entradas_dataframe.to_records()
        etapa_ciclo = EtapaCiclo.INICIO
        ciclos = []
        for indice in range(1, len(entradas)):
<<<<<<< HEAD
            actual = entradas[indice]
            anterior = entradas[indice - 1]
            if etapa_ciclo == EtapaCiclo.INICIO:
                etapa_ciclo = self.__evaluar_etapa_inicio(anterior, actual, ciclos)
=======
            anterior = entradas[indice - 1]
            actual = entradas[indice]
            if self.__comienza_nuevo_ciclo(anterior, actual, ciclos):
                etapa_ciclo = EtapaCiclo.EXCAVAR
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
            elif etapa_ciclo == EtapaCiclo.EXCAVAR:
                etapa_ciclo = self.__evaluar_etapa_excavar(actual, ciclos)
            elif etapa_ciclo == EtapaCiclo.TRANSPORTAR:
                etapa_ciclo = self.__evaluar_etapa_transportar(actual, ciclos)
            elif etapa_ciclo == EtapaCiclo.DESCARGAR:
<<<<<<< HEAD
                etapa_ciclo = self.__evaluar_etapa_descargar(actual, ciclos)
        return [ciclo for ciclo in ciclos if ciclo['fin'] != -1]
        
    def __evaluar_etapa_inicio(self, anterior, actual, ciclos):
        if actual['DIG_MODE'] == 1:
            if anterior['VELOCIDAD_HOIST_INV'] < self.umbral_cambio_velocidad_hoist and actual['VELOCIDAD_HOIST_INV'] >= self.umbral_cambio_velocidad_hoist:
                ciclos.append({
                    'fin': -1,
                    'excavar': [actual['ID']],
                    'transportar': [],
                    'descargar': []
                })
                return EtapaCiclo.EXCAVAR
        return EtapaCiclo.INICIO

    def __evaluar_etapa_excavar(self, actual, ciclos):
        ciclo = ciclos[len(ciclos) - 1]
        if actual['HOIST_IW_INV'] <= actual['HOIST_ROPE_LENGTH_INV'] and actual['HOIST_ROPE_LENGTH_INV'] >= self.umbral_largo_cable:
=======
                etapa_ciclo = self.__evaluar_etapa_descargar(anterior, actual, ciclos)
        return [ciclo for ciclo in ciclos if ciclo['fin'] != -1]
        
    def __comienza_nuevo_ciclo(self, anterior, actual, ciclos):
        if anterior['HOIST_SPEED_INV'] < self.umbral_cambio_velocidad_hoist and actual['HOIST_SPEED_INV'] >= self.umbral_cambio_velocidad_hoist and actual['HOIST_ROPE_LENGTH_INV'] < self.umbral_largo_cable_excavar and actual['DIG_MODE'] == 1:
            fin = anterior['ID'] if len(ciclos) > 1 else -1 
            ciclos.append({
                'EQUIPO_PESADO_ID': actual['MACHINE_IDENTIFIER'],
                'fin': fin,
                'excavar': [actual['ID']],
                'transportar': [],
                'descargar': []
            })
            return True
        return False

    def __evaluar_etapa_excavar(self, actual, ciclos):
        ciclo = ciclos[len(ciclos) - 1]
        if actual['HOIST_IW_INV'] <= actual['HOIST_ROPE_LENGTH_INV'] and actual['HOIST_ROPE_LENGTH_INV'] >= self.umbral_largo_cable_transportar:
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
            ciclo['transportar'].append(actual['ID'])
            return EtapaCiclo.TRANSPORTAR
        ciclo['excavar'].append(actual['ID'])
        return EtapaCiclo.EXCAVAR

    def __evaluar_etapa_transportar(self, actual, ciclos):
        ciclo = ciclos[len(ciclos) - 1]
        if actual['DIPEER_TRIP'] == 1:
            ciclo['descargar'].append(actual['ID'])
            return EtapaCiclo.DESCARGAR
        ciclo['transportar'].append(actual['ID'])
        return EtapaCiclo.TRANSPORTAR

<<<<<<< HEAD
    def __evaluar_etapa_descargar(self, actual, ciclos):
        ciclo = ciclos[len(ciclos) - 1]
        if actual['DIG_MODE'] == 0:
=======
    def __evaluar_etapa_descargar(self, anterior, actual, ciclos):
        ciclo = ciclos[len(ciclos) - 1]
        if actual['DIG_MODE'] == 0 and anterior['DIG_MODE'] == 1:
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
            ciclo['fin'] = actual['ID']
            return EtapaCiclo.INICIO
        ciclo['descargar'].append(actual['ID'])
        return EtapaCiclo.DESCARGAR
<<<<<<< HEAD
=======

>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
