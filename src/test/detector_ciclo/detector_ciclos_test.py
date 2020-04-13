import pytest
import pandas as pd
import numpy as np

from src.detector_ciclo.detector_ciclos import DetectorCiclos

detector_ciclos = DetectorCiclos({
    'umbral_cambio_velocidad_hoist': 0.502,
    'umbral_largo_cable_excavar': 0.4,
    'umbral_largo_cable_transportar': 0.4616
})

def test_procesar_registros_con_un_ciclo_entero():
    # Given
    entradas_dataframe = pd.DataFrame(
        columns = ['ID', 'DIG_MODE', 'HOIST_SPEED_INV', 'HOIST_IW_INV', 'HOIST_ROPE_LENGTH_INV', 'DIPEER_TRIP'],
        data = np.array(
            [
                [1,  0,  0.4, 0.0,  0.0,  0], # INICIO
                [2,  1,  0.6, 0.0,  0.0,  0], # 0.4 < 0.502 and 0.6 >= 0.502 ✔️ INICIO -> EXCAVAR
                [3,  1,  0.6, 0.0,  0.0,  0], # 0.0 < 0.0   and 0.0 >= 0.4   ❌ EXCAVAR
                [4,  1,  0.6, 0.0,  0.0,  0], # 0.0 < 0.0   and 0.0 >= 0.4   ❌ EXCAVAR
                [5,  1,  0.6, 0.1,  0.5,  0], # 0.1 < 0.5   and 0.5 >= 0.4   ✔️ EXCAVAR -> TRANSPORTAR
                [6,  1,  0.0, 0.1,  0.5,  0], # 0 == 1                       ❌ TRANSPORTAR
                [7,  1,  0.0, 0.1,  0.5,  0], # 0 == 1                       ❌ TRANSPORTAR
                [8,  1,  0.0, 0.0,  0.0,  0], # 0 == 1                       ❌ TRANSPORTAR
                [9,  1,  0.0, 0.0,  0.0,  1], # 1 == 1                       ✔️ TRANSPORTAR -> DESCARGAR
                [10, 1,  0.0, 0.0,  0.0,  1], # 1 == 0                       ❌ DESCARGAR
                [11, 1,  0.0, 0.0,  0.0,  1], # 1 == 0                       ❌ DESCARGAR
                [12, 0,  0.0, 0.0,  0.0,  0], # 0 == 0                       ✔️ DESCARGAR -> INICIO
            ]
        )
    )
    entradas_dataframe['MACHINE_IDENTIFIER'] = 'Shovel01'
    
    # When
    ciclos = detector_ciclos.detectar_ciclos(entradas_dataframe)

    # Then
    assert ciclos == [
        {
            'EQUIPO_PESADO_ID': 'Shovel01',
            'fin': 12,
            'excavar': [2, 3, 4],
            'transportar': [5, 6, 7, 8],
            'descargar': [9, 10, 11]
        }
    ]


def test_procesar_registros_con_varios_ciclos_enteros():
    # Given
    entradas_dataframe = pd.DataFrame(
        columns = ['ID', 'DIG_MODE', 'HOIST_SPEED_INV', 'HOIST_IW_INV', 'HOIST_ROPE_LENGTH_INV', 'DIPEER_TRIP'],
        data = np.array(
            [
                [1,  0,  0.4, 0.0,  0.0,  0], # INICIO
                [2,  1,  0.6, 0.0,  0.0,  0], # 0.4 < 0.502 and 0.6 >= 0.502 ✔️ INICIO -> EXCAVAR
                [3,  1,  0.6, 0.0,  0.0,  0], # 0.0 < 0.0   and 0.0 >= 0.4   ❌ EXCAVAR
                [4,  1,  0.6, 0.0,  0.0,  0], # 0.0 < 0.0   and 0.0 >= 0.4   ❌ EXCAVAR
                [5,  1,  0.6, 0.1,  0.5,  0], # 0.1 < 0.5   and 0.5 >= 0.4   ✔️ EXCAVAR -> TRANSPORTAR
                [6,  1,  0.0, 0.1,  0.5,  0], # 0 == 1                       ❌ TRANSPORTAR
                [7,  1,  0.0, 0.1,  0.5,  0], # 0 == 1                       ❌ TRANSPORTAR
                [8,  1,  0.0, 0.0,  0.0,  0], # 0 == 1                       ❌ TRANSPORTAR
                [9,  1,  0.0, 0.0,  0.0,  1], # 1 == 1                       ✔️ TRANSPORTAR -> DESCARGAR
                [10, 1,  0.0, 0.0,  0.0,  1], # 1 == 0                       ❌ DESCARGAR
                [11, 1,  0.0, 0.0,  0.0,  1], # 1 == 0                       ❌ DESCARGAR
                [12, 0,  0.5, 0.0,  0.0,  0], # 0 == 0                       ✔️ DESCARGAR -> INICIO
                [13, 1,  0.7, 0.0,  0.0,  0], # 0.5 < 0.502 and 0.7 >= 0.502 ✔️ INICIO -> EXCAVAR
                [14, 1,  0.7, 0.0,  0.0,  0], # 0.0 < 0.0   and 0.0 >= 0.4   ❌ EXCAVAR
                [15, 1,  0.7, 0.0,  0.0,  0], # 0.0 < 0.0   and 0.0 >= 0.4   ❌ EXCAVAR
                [16, 1,  0.7, 0.2,  0.6,  0], # 0.2 < 0.6   and 0.6 >= 0.4   ✔️ EXCAVAR -> TRANSPORTAR
                [17, 1,  0.0, 0.2,  0.6,  0], # 0 == 1                       ❌ TRANSPORTAR
                [18, 1,  0.0, 0.2,  0.6,  0], # 0 == 1                       ❌ TRANSPORTAR
                [19, 1,  0.0, 0.0,  0.0,  0], # 0 == 1                       ❌ TRANSPORTAR
                [20, 1,  0.0, 0.0,  0.0,  1], # 1 == 1                       ✔️ TRANSPORTAR -> DESCARGAR
                [21, 1,  0.0, 0.0,  0.0,  1], # 1 == 0                       ❌ DESCARGAR
                [22, 1,  0.0, 0.0,  0.0,  1], # 1 == 0                       ❌ DESCARGAR
                [23, 0,  0.0, 0.0,  0.0,  0], # 0 == 0                       ✔️ DESCARGAR -> INICIO
                [24, 0,  0.0, 0.0,  0.0,  0], # 0.0 < 0.502 and 0.0 >= 0.502 ❌ INICIO
                [25, 0,  0.0, 0.0,  0.0,  0], # 0.0 < 0.502 and 0.0 >= 0.502 ❌ INICIO
                [26, 1,  0.9, 0.0,  0.0,  0], # 0.0 < 0.502 and 0.9 >= 0.502 ✔️ INICIO -> EXCAVAR
                [27, 1,  0.8, 0.0,  0.0,  0], # 0.0 < 0.0   and 0.0 >= 0.4   ❌ EXCAVAR
                [28, 1,  0.7, 0.0,  0.0,  0], # 0.0 < 0.0   and 0.0 >= 0.4   ❌ EXCAVAR
                [29, 1,  0.6, 0.1,  0.8,  0], # 0.1 < 0.8   and 0.8 >= 0.4   ✔️ EXCAVAR -> TRANSPORTAR
                [30, 1,  0.0, 0.1,  0.5,  0], # 0 == 1                       ❌ TRANSPORTAR
                [31, 1,  0.0, 0.1,  0.5,  0], # 0 == 1                       ❌ TRANSPORTAR
                [32, 1,  0.0, 0.0,  0.5,  0], # 0 == 1                       ❌ TRANSPORTAR
                [33, 1,  0.0, 0.0,  0.0,  1], # 1 == 1                       ✔️ TRANSPORTAR -> DESCARGAR
                [34, 1,  0.0, 0.0,  0.0,  1], # 1 == 0                       ❌ DESCARGAR
                [35, 1,  0.0, 0.0,  0.0,  1], # 1 == 0                       ❌ DESCARGAR
                [36, 0,  0.0, 0.0,  0.0,  0]  # 0 == 0                       ✔️ DESCARGAR -> INICIO
            ]
        )
    )
    entradas_dataframe['MACHINE_IDENTIFIER'] = 'Shovel01'
    
    # When
    ciclos = detector_ciclos.detectar_ciclos(entradas_dataframe)

    # Then
    assert ciclos == [
        {
            'EQUIPO_PESADO_ID': 'Shovel01',
            'fin': 12,
            'excavar': [2, 3, 4],
            'transportar': [5, 6, 7, 8],
            'descargar': [9, 10, 11]
        },
        {
            'EQUIPO_PESADO_ID': 'Shovel01',
            'fin': 23,
            'excavar': [13, 14, 15],
            'transportar': [16, 17, 18, 19],
            'descargar': [20, 21, 22]
        },
        {
            'EQUIPO_PESADO_ID': 'Shovel01',
            'fin': 36,
            'excavar': [26, 27, 28],
            'transportar': [29, 30, 31, 32],
            'descargar': [33, 34, 35]
        }
    ]


def test_procesar_registros_con_ciclo_entero_y_ciclo_incompleto():
    # Given
    entradas_dataframe = pd.DataFrame(
        columns = ['ID', 'DIG_MODE', 'HOIST_SPEED_INV', 'HOIST_IW_INV', 'HOIST_ROPE_LENGTH_INV', 'DIPEER_TRIP'],
        data = np.array(
            [
                [1,  0,  0.2, 0.0,  0.0,  0], # INICIO
                [2,  1,  0.9, 0.0,  0.0,  0], # 0.2 < 0.502 and 0.9 >= 0.502 ✔️ INICIO -> EXCAVAR
                [3,  1,  0.6, 0.0,  0.3,  0], # 0.0 < 0.3   and 0.3 >= 0.4   ❌ EXCAVAR
                [4,  1,  0.6, 0.1,  0.2,  0], # 0.1 < 0.2   and 0.2 >= 0.4   ❌ EXCAVAR
                [5,  1,  0.6, 0.1,  0.7,  0], # 0.1 < 0.7   and 0.7 >= 0.4   ✔️ EXCAVAR -> TRANSPORTAR
                [6,  1,  0.0, 0.1,  0.5,  0], # 0 == 1                       ❌ TRANSPORTAR
                [7,  1,  0.0, 0.1,  0.5,  0], # 0 == 1                       ❌ TRANSPORTAR
                [8,  1,  0.0, 0.0,  0.0,  0], # 0 == 1                       ❌ TRANSPORTAR
                [9,  1,  0.0, 0.0,  0.0,  1], # 1 == 1                       ✔️ TRANSPORTAR -> DESCARGAR
                [10, 1,  0.0, 0.0,  0.0,  1], # 1 == 0                       ❌ DESCARGAR
                [11, 1,  0.0, 0.0,  0.0,  1], # 1 == 0                       ❌ DESCARGAR
                [12, 0,  0.1, 0.0,  0.0,  0], # 0 == 0                       ✔️ DESCARGAR -> INICIO
                [13, 1,  0.8, 0.0,  0.0,  0], # 0.1 < 0.502 and 0.8 >= 0.502 ✔️ INICIO -> EXCAVAR
                [14, 1,  0.6, 0.1,  0.2,  0], # 0.1 < 0.2   and 0.2 >= 0.4   ❌ EXCAVAR
                [15, 1,  0.6, 0.1,  0.2,  0], # 0.1 < 0.2   and 0.2 >= 0.4   ❌ EXCAVAR
                [16, 1,  0.6, 0.3,  0.5,  0], # 0.3 < 0.5   and 0.5 >= 0.4   ✔️ EXCAVAR -> TRANSPORTAR
                [17, 1,  0.0, 0.1,  0.5,  0], # 0 == 1                       ❌ TRANSPORTAR
                
            ]
        )
    )
    entradas_dataframe['MACHINE_IDENTIFIER'] = 'Shovel01'
    
    # When
    ciclos = detector_ciclos.detectar_ciclos(entradas_dataframe)

    # Then
    assert ciclos == [
        {
            'EQUIPO_PESADO_ID': 'Shovel01',
            'fin': 12,
            'excavar': [2, 3, 4],
            'transportar': [5, 6, 7, 8],
            'descargar': [9, 10, 11]
        }
    ]


def test_procesar_registros_con_ciclo_incompleto():
    # Given
    entradas_dataframe = pd.DataFrame(
        columns = ['ID', 'DIG_MODE', 'HOIST_SPEED_INV', 'HOIST_IW_INV', 'HOIST_ROPE_LENGTH_INV', 'DIPEER_TRIP'],
        data = np.array(
            [
                [1,  0,  0.2, 0.0,  0.0,  0], # INICIO
                [2,  1,  0.9, 0.0,  0.0,  0], # 0.2 < 0.502 and 0.9 >= 0.502 ✔️ INICIO -> EXCAVAR
                [3,  1,  0.6, 0.0,  0.3,  0], # 0.0 < 0.3   and 0.3 >= 0.4   ❌ EXCAVAR
                [4,  1,  0.6, 0.1,  0.2,  0], # 0.1 < 0.2   and 0.2 >= 0.4   ❌ EXCAVAR
                [5,  1,  0.6, 0.1,  0.7,  0], # 0.1 < 0.7   and 0.7 >= 0.4   ✔️ EXCAVAR -> TRANSPORTAR
                [6,  1,  0.0, 0.1,  0.5,  0], # 0 == 1                       ❌ TRANSPORTAR
                [7,  1,  0.0, 0.1,  0.5,  0], # 0 == 1                       ❌ TRANSPORTAR
                [8,  1,  0.0, 0.0,  0.0,  0], # 0 == 1                       ❌ TRANSPORTAR
                [9,  1,  0.0, 0.0,  0.0,  1], # 1 == 1                       ✔️ TRANSPORTAR -> DESCARGAR
                [10, 1,  0.0, 0.0,  0.0,  1]  # 1 == 0                       ❌ DESCARGAR
            ]
        )
    )
    entradas_dataframe['MACHINE_IDENTIFIER'] = 'Shovel01'
    
    # When
    ciclos = detector_ciclos.detectar_ciclos(entradas_dataframe)

    # Then
    assert ciclos == []


def test_procesar_registros_sin_ciclos():
    # Given
    entradas_dataframe = pd.DataFrame(
        columns = ['ID', 'DIG_MODE', 'HOIST_SPEED_INV', 'HOIST_IW_INV', 'HOIST_ROPE_LENGTH_INV', 'DIPEER_TRIP'],
        data = np.array(
            [
                [1,  0,  0.2, 0.0,  0.0,  0], # INICIO
                [2,  1,  0.3, 0.0,  0.0,  0], # 0.2 < 0.502 and 0.3 >= 0.502 ❌ INICIO
                [3,  1,  0.4, 0.0,  0.3,  0], # 0.3 < 0.502 and 0.4 >= 0.502 ❌ INICIO
                [4,  1,  0.4, 0.1,  0.2,  0], # 0.4 < 0.502 and 0.4 >= 0.502 ❌ INICIO
                [5,  1,  0.5, 0.1,  0.7,  0], # 0.5 < 0.502 and 0.5 >= 0.502 ❌ INICIO
                [6,  1,  0.5, 0.1,  0.5,  0], # 0.5 < 0.502 and 0.5 >= 0.502 ❌ INICIO
                [7,  1,  0.5, 0.1,  0.5,  0], # 0.5 < 0.502 and 0.5 >= 0.502 ❌ INICIO
                [8,  1,  0.5, 0.0,  0.0,  0], # 0.5 < 0.502 and 0.5 >= 0.502 ❌ INICIO
                [9,  1,  0.5, 0.0,  0.0,  1], # 0.5 < 0.502 and 0.5 >= 0.502 ❌ INICIO
                [10, 1,  0.5, 0.0,  0.0,  1]  # 0.5 < 0.502 and 0.5 >= 0.502 ❌ INICIO
            ]
        )
    )
    entradas_dataframe['MACHINE_IDENTIFIER'] = 'Shovel01'
    
    # When
    ciclos = detector_ciclos.detectar_ciclos(entradas_dataframe)

    # Then
    assert ciclos == []
