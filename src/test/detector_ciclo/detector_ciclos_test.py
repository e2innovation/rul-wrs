import pytest
import pandas as pd
import numpy as np

from src.detector_ciclo.detector_ciclos import DetectorCiclos

def test_procesar_registros_con_un_ciclo_entero():
    # Given
    entradas_dataframe = pd.DataFrame(
        data = np.array(
            [
                [1,  0,  0.4, 0.0,  0.0,  0],
                [2,  1,  0.6, 0.0,  0.0,  0],
                [3,  1,  0.6, 0.0,  0.0,  0],
                [4,  1,  0.6, 0.0,  0.0,  0],
                [5,  1,  0.6, 0.1,  0.5,  0],
                [6,  1,  0.0, 0.1,  0.5,  0],
                [7,  1,  0.0, 0.1,  0.5,  0],
                [8,  1,  0.0, 0.0,  0.0,  0],
                [9,  1,  0.0, 0.0,  0.0,  1],
                [10, 1,  0.0, 0.0,  0.0,  1],
                [11, 1,  0.0, 0.0,  0.0,  1],
                [12, 0,  0.0, 0.0,  0.0,  0],
            ]
        ),
        columns = ['ID', 'DIG_MODE', 'VELOCIDAD_HOIST_INV', 'HOIST_IW_INV', 'HOIST_ROPE_LENGTH_INV', 'DIPEER_TRIP']
    )
    detector_ciclos = DetectorCiclos({
        'umbral_cambio_velocidad_hoist': 0.502,
        'umbral_largo_cable': 0.4
    })

    # When
    ciclos = detector_ciclos.detectar_ciclos(entradas_dataframe)

    # Then
    assert ciclos == [
        {
            'fin': 12,
            'excavar': [2, 3, 4],
            'transportar': [5, 6, 7, 8],
            'descargar': [9, 10, 11]
        }
    ]

def test_procesar_registros_con_varios_ciclos_enteros():
    # Given
    entradas_dataframe = pd.DataFrame(
        data = np.array(
            [
                [1,  0,  0.4, 0.0,  0.0,  0],
                [2,  1,  0.6, 0.0,  0.0,  0],
                [3,  1,  0.6, 0.0,  0.0,  0],
                [4,  1,  0.6, 0.0,  0.0,  0],
                [5,  1,  0.6, 0.1,  0.5,  0],
                [6,  1,  0.0, 0.1,  0.5,  0],
                [7,  1,  0.0, 0.1,  0.5,  0],
                [8,  1,  0.0, 0.0,  0.0,  0],
                [9,  1,  0.0, 0.0,  0.0,  1],
                [10, 1,  0.0, 0.0,  0.0,  1],
                [11, 1,  0.0, 0.0,  0.0,  1],
                [12, 0,  0.0, 0.0,  0.0,  0],
                [13, 1,  0.7, 0.0,  0.0,  0],
                [14, 1,  0.7, 0.0,  0.0,  0],
                [15, 1,  0.7, 0.0,  0.0,  0],
                [16, 1,  0.7, 0.2,  0.6,  0],
                [17, 1,  0.0, 0.2,  0.6,  0],
                [18, 1,  0.0, 0.2,  0.6,  0],
                [19, 1,  0.0, 0.0,  0.0,  0],
                [20, 1,  0.0, 0.0,  0.0,  1],
                [21, 1,  0.0, 0.0,  0.0,  1],
                [22, 1,  0.0, 0.0,  0.0,  1],
                [23, 0,  0.0, 0.0,  0.0,  0],
                [24, 0,  0.0, 0.0,  0.0,  0],
                [25, 0,  0.0, 0.0,  0.0,  0],
                [26, 1,  0.7, 0.0,  0.0,  0],
                [27, 1,  0.7, 0.0,  0.0,  0],
                [28, 1,  0.7, 0.0,  0.0,  0],
                [29, 1,  0.6, 0.1,  0.5,  0],
                [30, 1,  0.0, 0.1,  0.5,  0],
                [31, 1,  0.0, 0.1,  0.5,  0],
                [32, 1,  0.0, 0.0,  0.5,  0],
                [33, 1,  0.0, 0.0,  0.0,  1],
                [34, 1,  0.0, 0.0,  0.0,  1],
                [35, 1,  0.0, 0.0,  0.0,  1],
                [36, 0,  0.0, 0.0,  0.0,  0]
            ]
        ),
        columns = ['ID', 'DIG_MODE', 'VELOCIDAD_HOIST_INV', 'HOIST_IW_INV', 'HOIST_ROPE_LENGTH_INV', 'DIPEER_TRIP']
    )
    detector_ciclos = DetectorCiclos({
        'umbral_cambio_velocidad_hoist': 0.502,
        'umbral_largo_cable': 0.4
    })

    # When
    ciclos = detector_ciclos.detectar_ciclos(entradas_dataframe)

    # Then
    assert ciclos == [
        {
            'fin': 12,
            'excavar': [2, 3, 4],
            'transportar': [5, 6, 7, 8],
            'descargar': [9, 10, 11]
        },
        {
            'fin': 23,
            'excavar': [13, 14, 15],
            'transportar': [16, 17, 18, 19],
            'descargar': [20, 21, 22]
        },
        {
            'fin': 36,
            'excavar': [26, 27, 28],
            'transportar': [29, 30, 31, 32],
            'descargar': [33, 34, 35]
        }
    ]

def test_procesar_registros_con_ciclo_entero_y_ciclo_incompleto():
    # Given
    entradas_dataframe = pd.DataFrame(
        data = np.array(
            [
                [1,  0,  0.4, 0.0,  0.0,  0],
                [2,  1,  0.6, 0.0,  0.0,  0],
                [3,  1,  0.6, 0.0,  0.0,  0],
                [4,  1,  0.6, 0.0,  0.0,  0],
                [5,  1,  0.6, 0.1,  0.5,  0],
                [6,  1,  0.0, 0.1,  0.5,  0],
                [7,  1,  0.0, 0.1,  0.5,  0],
                [8,  1,  0.0, 0.0,  0.0,  0],
                [9,  1,  0.0, 0.0,  0.0,  1],
                [10, 1,  0.0, 0.0,  0.0,  1],
                [11, 1,  0.0, 0.0,  0.0,  1],
                [12, 0,  0.0, 0.0,  0.0,  0],
                [13, 1,  0.6, 0.0,  0.0,  0],
                [14, 1,  0.6, 0.0,  0.0,  0],
                [15, 1,  0.6, 0.0,  0.0,  0],
                [16, 1,  0.6, 0.1,  0.5,  0],
                [17, 1,  0.0, 0.1,  0.5,  0],
                
            ]
        ),
        columns = ['ID', 'DIG_MODE', 'VELOCIDAD_HOIST_INV', 'HOIST_IW_INV', 'HOIST_ROPE_LENGTH_INV', 'DIPEER_TRIP']
    )
    detector_ciclos = DetectorCiclos({
        'umbral_cambio_velocidad_hoist': 0.502,
        'umbral_largo_cable': 0.4
    })

    # When
    ciclos = detector_ciclos.detectar_ciclos(entradas_dataframe)

    # Then
    assert ciclos == [
        {
            'fin': 12,
            'excavar': [2, 3, 4],
            'transportar': [5, 6, 7, 8],
            'descargar': [9, 10, 11]
        }
    ]