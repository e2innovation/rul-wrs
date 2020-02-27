import pytest
import pandas as pd
from pandas._testing import assert_frame_equal
from pandas._testing import assert_series_equal

from util.formatea_entrada import FormateaEntrada


def test_generar_dataframe_con_formato_desde_registros_entrada():
    # Given
    registros_entrada = [
        {
            'ID': 1,
            'EQUIPO_PESADO_ID': 'pala01',
            'FECHA_HORA': '2020-01-15T13:45:30',
            'REGISTRO': """{
                \"field01\": \"value01\",
                \"field02\": \"value02\",
                \"field03\": \"value03\"
            }"""
        },
        {
            'ID': 2,
            'EQUIPO_PESADO_ID': 'pala01',
            'FECHA_HORA': '2020-01-15T13:46:30',
            'REGISTRO': """{
                \"field01\": \"value04\",
                \"field02\": \"value05\",
                \"field03\": \"value06\"
            }"""
        },
        {
            'ID': 3,
            'EQUIPO_PESADO_ID': 'pala01',
            'FECHA_HORA': '2020-01-15T13:47:30',
            'REGISTRO': """{
                \"field01\": \"value07\",
                \"field02\": \"value08\",
                \"field03\": \"value09\"
            }"""
        }
    ]

    # When
    salida = FormateaEntrada.registros_a_dataframe(registros_entrada)

    # Then
    resultado_esperado = pd.DataFrame({
            'field01': ['value01', 'value04', 'value07'],
            'field02': ['value02', 'value05', 'value08'],
            'field03': ['value03', 'value06', 'value09'],
            'ID': [1, 2, 3]
        },
        index=['2020-01-15T13:45:30', '2020-01-15T13:46:30', '2020-01-15T13:47:30']
    )
    assert_frame_equal(salida, resultado_esperado)
    

def test_generar_campos_inv_desde_dataframe():
    # Given
    dataframe = pd.DataFrame({
            'LONGITUD_CABLE_HOIST': [20, 25, 30],
            'VELOCIDAD_HOIST': [30.0, 35.3, 40.2],
            'BYTE_ESTATUS_3': [12, 10, 9],
            'TORQUE_HOIST': [10, 11, 12],
            'CORRIENTE_IW_HOIST': [23, 30, 40]
        }
    )

    # When
    FormateaEntrada.generar_campos_inv(dataframe)

    # Then
    resultado_esperado = pd.DataFrame({
            'LONGITUD_CABLE_HOIST_INV': [-20, -25, -30],
            'VELOCIDAD_HOIST_INV': [-3.0, -3.53, -4.02],
            'DIG_MODE': [0, 2, 0],
            'DIPEER_TRIP': [0, 0, 1],
            'TORQUE_HOIST_INV': [-10, -11, -12],
            'CORRIENTE_IW_HOIST_INV': [-23, -30, -40]
        }
    )
    assert_series_equal(dataframe['LONGITUD_CABLE_HOIST_INV'], resultado_esperado['LONGITUD_CABLE_HOIST_INV'])
    assert_series_equal(dataframe['VELOCIDAD_HOIST_INV'], resultado_esperado['VELOCIDAD_HOIST_INV'])
    assert_series_equal(dataframe['DIG_MODE'], resultado_esperado['DIG_MODE'])
    assert_series_equal(dataframe['DIPEER_TRIP'], resultado_esperado['DIPEER_TRIP'])
    assert_series_equal(dataframe['TORQUE_HOIST_INV'], resultado_esperado['TORQUE_HOIST_INV'])
    assert_series_equal(dataframe['CORRIENTE_IW_HOIST_INV'], resultado_esperado['CORRIENTE_IW_HOIST_INV'])


def test_normalizar_campo_de_dataframe():
    # Given
    dataframe = pd.DataFrame({
            'campo1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            'campo2': [-1, -2, -3, -4, -5, -6, -7, -8, -9, 0],
            'campo3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'campo4': [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
        }
    )

    campos_a_normalizar = ['campo1', 'campo2', 'campo3', 'campo4']

    # When
    FormateaEntrada.normalizar_campos(dataframe, campos_a_normalizar)

    # Then
    resultado_esperado = pd.DataFrame({
            'campo1': [1/9, 2/9, 3/9, 4/9, 5/9, 6/9, 7/9, 8/9, 1.0, 0.0],
            'campo2': [8/9, 7/9, 6/9, 5/9, 4/9, 3/9, 2/9, 1/9, 0.0, 1.0],
            'campo3': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            'campo4': [0.0, 1/9, 2/9, 3/9, 4/9, 5/9, 6/9, 7/9, 8/9, 1.0],
        }
    )
    assert_series_equal(dataframe['campo1'], resultado_esperado['campo1'])
    assert_series_equal(dataframe['campo2'], resultado_esperado['campo2'])
    assert_series_equal(dataframe['campo3'], resultado_esperado['campo3'])
    assert_series_equal(dataframe['campo4'], resultado_esperado['campo4'])
    