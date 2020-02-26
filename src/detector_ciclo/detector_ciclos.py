from src.util.etapa_ciclo import EtapaCiclo

class DetectorCiclos:
    def __init__(self, configuracion):
        self.umbral_cambio_velocidad_hoist = configuracion['umbral_cambio_velocidad_hoist']
        self.umbral_largo_cable = configuracion['umbral_largo_cable']
        
    def detectar_ciclos(self, entradas_dataframe):
        entradas = entradas_dataframe.to_records()
        etapa_ciclo = EtapaCiclo.INICIO
        ciclos = []
        for indice in range(1, len(entradas)):
            actual = entradas[indice]
            anterior = entradas[indice - 1]
            if etapa_ciclo == EtapaCiclo.INICIO:
                etapa_ciclo = self.__evaluar_etapa_inicio(anterior, actual, ciclos)
            elif etapa_ciclo == EtapaCiclo.EXCAVAR:
                etapa_ciclo = self.__evaluar_etapa_excavar(actual, ciclos)
            elif etapa_ciclo == EtapaCiclo.TRANSPORTAR:
                etapa_ciclo = self.__evaluar_etapa_transportar(actual, ciclos)
            elif etapa_ciclo == EtapaCiclo.DESCARGAR:
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

    def __evaluar_etapa_descargar(self, actual, ciclos):
        ciclo = ciclos[len(ciclos) - 1]
        if actual['DIG_MODE'] == 0:
            ciclo['fin'] = actual['ID']
            return EtapaCiclo.INICIO
        ciclo['descargar'].append(actual['ID'])
        return EtapaCiclo.DESCARGAR
