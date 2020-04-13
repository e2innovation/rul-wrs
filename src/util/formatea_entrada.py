import pandas as pd
import json

class FormateaEntrada:
    def __init__(self):
        pass

    @staticmethod
    def registros_a_dataframe(registros):
        entrada = pd.DataFrame(registros, columns=['ID', 'FECHA_HORA', 'REGISTRO'])
        entrada['REGISTRO_JSON'] = entrada['REGISTRO'].apply(json.loads)
        salida = pd.DataFrame.from_records(entrada['REGISTRO_JSON'].values, index=entrada['FECHA_HORA'].values)
        salida['ID'] = entrada['ID'].values
        return salida

    @staticmethod
    def generar_campos_inv(dataframe):
        dataframe['HOIST_ROPE_LENGTH_INV'] = dataframe[['HOIST_ROPE_LENGTH']].apply(lambda x : x * -1)
        dataframe['HOIST_SPEED_INV'] = dataframe.loc[:,'HOIST_SPEED'].apply(lambda x : x * -0.1)
        dataframe['DIG_MODE'] = dataframe.loc[:,'STATUS_BYTE_3'].apply(lambda x : int(x) & 2) # nos indica que se encuentra en modo excavación
        dataframe['DIPEER_TRIP'] = dataframe.loc[:,'STATUS_BYTE_3'].apply(lambda x : x & 1) # se activa con la orden de apertura de compuerta de balde
        dataframe['HOIST_TORQUE_INV'] = dataframe[['HOIST_TORQUE']].apply(lambda x : x * -1)
        dataframe['HOIST_IW_INV'] = dataframe[['HOIST_IW']].apply(lambda x : x * -1)
        return dataframe

    @staticmethod
    def normalizar_campos(dataframe, campos):
        dataframe[campos] = dataframe[campos].apply(lambda x:(x-x.min()) / (1 if x.max()-x.min() == 0 else x.max()-x.min()))
    
