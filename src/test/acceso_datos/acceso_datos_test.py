import pytest
from unittest.mock import MagicMock
from unittest.mock import Mock
from acceso_datos.acceso_datos import AccesoDatos
from util.estado_equipo_pesado import EstadoEquipoPesado

def test_seleccionar_equipos_pesados_obtener_solo_equipos_que_esten_apagados_o_funcionando():
    # Mock / Given
    resultado_procedimiento_almacenado = [
        [
            {
                "EQUIPO_PESADO_ID": "Shovel01",
                "TIPO": "PALA",
                "DESCRIPCION": "DESCRIPCION DUMMY Shovel 01",
                "ESTADO": EstadoEquipoPesado.FUNCIONANDO.value,
                "REPORTE": "{ 'id': 'dummy report 01' }"
            },
            {
                "EQUIPO_PESADO_ID": "Shovel02",
                "TIPO": "PALA",
                "DESCRIPCION": "DESCRIPCION DUMMY Shovel 02",
                "ESTADO": EstadoEquipoPesado.APAGADO.value,
                "REPORTE": "{ 'id': 'dummy report 02' }"
            },
            {
                "EQUIPO_PESADO_ID": "Shovel03",
                "TIPO": "PALA",
                "DESCRIPCION": "DESCRIPCION DUMMY Shovel 03",
                "ESTADO": EstadoEquipoPesado.FUNCIONANDO.value,
                "REPORTE": "{ 'id': 'dummy report 03' }"
            },
            {
                "EQUIPO_PESADO_ID": "Shovel04",
                "TIPO": "PALA",
                "DESCRIPCION": "DESCRIPCION DUMMY Shovel 04",
                "ESTADO": EstadoEquipoPesado.BAJA.value,
                "REPORTE": "{ 'id': 'dummy report 04' }"
            }
        ]
    ]

    bd_cliente = Mock()
    bd_cliente.ejecutar_procedimiento_almacenado = MagicMock(return_value = resultado_procedimiento_almacenado)
    acceso_datos = AccesoDatos(bd_cliente)

    # When
    resultado = acceso_datos.seleccionar_equipos_pesados_activos()

    # Then
    bd_cliente.ejecutar_procedimiento_almacenado.assert_called_once()
    assert resultado == [
        {
            "EQUIPO_PESADO_ID": "Shovel01",
            "TIPO": "PALA",
            "DESCRIPCION": "DESCRIPCION DUMMY Shovel 01",
            "ESTADO": EstadoEquipoPesado.FUNCIONANDO,
            "REPORTE": "{ 'id': 'dummy report 01' }"
        },
        {
            "EQUIPO_PESADO_ID": "Shovel02",
            "TIPO": "PALA",
            "DESCRIPCION": "DESCRIPCION DUMMY Shovel 02",
            "ESTADO": EstadoEquipoPesado.APAGADO,
            "REPORTE": "{ 'id': 'dummy report 02' }"
        },
        {
            "EQUIPO_PESADO_ID": "Shovel03",
            "TIPO": "PALA",
            "DESCRIPCION": "DESCRIPCION DUMMY Shovel 03",
            "ESTADO": EstadoEquipoPesado.FUNCIONANDO,
            "REPORTE": "{ 'id': 'dummy report 03' }"
        }
    ]

def test_no_hay_equipos_pesados_apagados_o_funcionando_entonces_retorna_lista_vacia():
    # Mock / Given
    resultado_procedimiento_almacenado = [
        [
            {
                "EQUIPO_PESADO_ID": "Shovel01",
                "TIPO": "PALA",
                "DESCRIPCION": "DESCRIPCION DUMMY Shovel 01",
                "ESTADO": EstadoEquipoPesado.BAJA.value,
                "REPORTE": "{ 'id': 'dummy report 01' }"
            },
            {
                "EQUIPO_PESADO_ID": "Shovel02",
                "TIPO": "PALA",
                "DESCRIPCION": "DESCRIPCION DUMMY Shovel 02",
                "ESTADO": EstadoEquipoPesado.BAJA.value,
                "REPORTE": "{ 'id': 'dummy report 02' }"
            },
            {
                "EQUIPO_PESADO_ID": "Shovel03",
                "TIPO": "PALA",
                "DESCRIPCION": "DESCRIPCION DUMMY Shovel 03",
                "ESTADO": EstadoEquipoPesado.BAJA.value,
                "REPORTE": "{ 'id': 'dummy report 03' }"
            },
            {
                "EQUIPO_PESADO_ID": "Shovel04",
                "TIPO": "PALA",
                "DESCRIPCION": "DESCRIPCION DUMMY Shovel 04",
                "ESTADO": EstadoEquipoPesado.BAJA.value,
                "REPORTE": "{ 'id': 'dummy report 04' }"
            }
        ]
    ]

    bd_cliente = Mock()
    bd_cliente.ejecutar_procedimiento_almacenado = MagicMock(return_value=resultado_procedimiento_almacenado)
    acceso_datos = AccesoDatos(bd_cliente)

    # When
    resultado = acceso_datos.seleccionar_equipos_pesados_activos()

    # Then
    bd_cliente.ejecutar_procedimiento_almacenado.assert_called_once()
    assert resultado == []

def test_seleccionar_registros_entrada_de_equipo_pesado_entonces_retorna_registros_entrada_deserializados():
    # Mock / Given
    resultado_procedimiento_almacenado = [
        [
            {
                "ID": 1000000,
                "EQUIPO_PESADO_ID": "Shovel01",
<<<<<<< HEAD
                "FECHA_HORA": "2018-09-09 00:00:00.467",
                "REGISTRO": '{ "campo01": "dummy 001", "campo02": "dummy 002" }'
=======
<<<<<<< Updated upstream
                "FECHA_HORA": "2018-09-09 00:00:00.467",
                "REGISTRO": '{ "campo01": "dummy 001", "campo02": "dummy 002" }'
=======
                "FECHA_HORA": "2020-01-15T13:45:30",
                "REGISTRO": """{
                    "HOIST_ROPE_LENGTH": 20,
                    "HOIST_SPEED": 30.0,
                    "STATUS_BYTE_3": 12,
                    "HOIST_TORQUE": 10,
                    "HOIST_IW": 23,
                    "SWING_ANGLE": 2,
                    "HOIST_SPEED_REF": 13,
                    "HOIST_KW": 4,
                    "CROWD_EXTENSION": 2,
                    "CROWD_SPEED_REF": 10
                }"""
>>>>>>> Stashed changes
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
            },
            {
                "ID": 1000001,
                "EQUIPO_PESADO_ID": "Shovel01",
<<<<<<< HEAD
                "FECHA_HORA": "2018-09-09 00:00:01.467",
                "REGISTRO": '{ "campo01": "dummy 011", "campo02": "dummy 012" }'
=======
<<<<<<< Updated upstream
                "FECHA_HORA": "2018-09-09 00:00:01.467",
                "REGISTRO": '{ "campo01": "dummy 011", "campo02": "dummy 012" }'
=======
                "FECHA_HORA": "2020-01-15T13:45:31",
                "REGISTRO": """{
                    "HOIST_ROPE_LENGTH": 25,
                    "HOIST_SPEED": 10.0,
                    "STATUS_BYTE_3": 22,
                    "HOIST_TORQUE": 4,
                    "HOIST_IW": 14,
                    "SWING_ANGLE": 2,
                    "HOIST_SPEED_REF": 15,
                    "HOIST_KW": 8,
                    "CROWD_EXTENSION": 6,
                    "CROWD_SPEED_REF": 20
                }"""
            },
            {
                "ID": 1000002,
                "EQUIPO_PESADO_ID": "Shovel01",
                "FECHA_HORA": "2020-01-15T13:45:32",
                "REGISTRO": """{
                    "HOIST_ROPE_LENGTH": 21,
                    "HOIST_SPEED": 23.5,
                    "STATUS_BYTE_3": 23,
                    "HOIST_TORQUE": 3,
                    "HOIST_IW": 18,
                    "SWING_ANGLE": 1,
                    "HOIST_SPEED_REF": 20,
                    "HOIST_KW": 15,
                    "CROWD_EXTENSION": 60,
                    "CROWD_SPEED_REF": 40
                }"""
            },
            {
                "ID": 1000003,
                "EQUIPO_PESADO_ID": "Shovel01",
                "FECHA_HORA": "2020-01-15T13:45:33",
                "REGISTRO": """{
                    "HOIST_ROPE_LENGTH": 15,
                    "HOIST_SPEED": 21.0,
                    "STATUS_BYTE_3": 17,
                    "HOIST_TORQUE": 13,
                    "HOIST_IW": 11,
                    "SWING_ANGLE": 1,
                    "HOIST_SPEED_REF": 25,
                    "HOIST_KW": 18,
                    "CROWD_EXTENSION": 16,
                    "CROWD_SPEED_REF": 30
                }"""
            },
            {
                "ID": 1000004,
                "EQUIPO_PESADO_ID": "Shovel01",
                "FECHA_HORA": "2020-01-15T13:45:34",
                "REGISTRO": """{
                    "HOIST_ROPE_LENGTH": 31,
                    "HOIST_SPEED": 13.1,
                    "STATUS_BYTE_3": 10,
                    "HOIST_TORQUE": 6,
                    "HOIST_IW": 15,
                    "SWING_ANGLE": 4,
                    "HOIST_SPEED_REF": 22,
                    "HOIST_KW": 6,
                    "CROWD_EXTENSION": 7,
                    "CROWD_SPEED_REF": 10
                }"""
>>>>>>> Stashed changes
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
            }
        ]
    ]

    bd_cliente = Mock()
    bd_cliente.ejecutar_procedimiento_almacenado = MagicMock(return_value=resultado_procedimiento_almacenado)
    acceso_datos = AccesoDatos(bd_cliente)
    equipo_pesado_dummy = {
        "EQUIPO_PESADO_ID": "Shovel01"
    }

    # When
<<<<<<< HEAD
=======
<<<<<<< Updated upstream
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
    resultado = acceso_datos.seleccionar_registro_entrada(equipo_pesado_dummy)

    # Then
    bd_cliente.ejecutar_procedimiento_almacenado.assert_called_once()
    assert resultado == [
        {
            "ID": 1000000,
            "EQUIPO_PESADO_ID": "Shovel01",
            "FECHA_HORA": "2018-09-09 00:00:00.467",
            "REGISTRO": { 
                "campo01": "dummy 001",
                "campo02": "dummy 002"
            }
        },
        {
            "ID": 1000001,
            "EQUIPO_PESADO_ID": "Shovel01",
            "FECHA_HORA": "2018-09-09 00:00:01.467",
            "REGISTRO": {
                "campo01": "dummy 011",
                "campo02": "dummy 012"
            }
        }
    ]
<<<<<<< HEAD
=======
=======
    resultado = acceso_datos.seleccionar_registros_entrada(equipo_pesado_dummy)
    
    # Then
    resultado_esperado = pd.DataFrame(
        data = {
            "SWING_ANGLE": [0.333333, 0.333333, 0.000000, 0.000000, 1.000000],
            "STATUS_BYTE_3": [12, 22, 23, 17, 10],
            "HOIST_IW": [23, 14, 18, 11, 15],
            "CROWD_EXTENSION": [0.000000, 0.068966, 1.000000, 0.241379, 0.086207],
            "HOIST_ROPE_LENGTH": [20, 25, 21, 15, 31],
            "HOIST_KW": [0.000000, 0.285714, 0.785714, 1.000000, 0.142857],
            "HOIST_TORQUE": [10, 4, 3, 13, 6],
            "HOIST_SPEED": [30.0, 10.0, 23.5, 21.0, 13.1],
            "CROWD_SPEED_REF": [0.000000, 0.333333, 1.000000, 0.666667, 0.000000],
            "HOIST_SPEED_REF": [0.000000, 0.166667, 0.583333, 1.000000, 0.750000],
            "ID": [1000000, 1000001, 1000002, 1000003, 1000004],
            "HOIST_ROPE_LENGTH_INV": [0.6875, 0.3750, 0.6250, 1.0000, 0.0000],
            "HOIST_SPEED_INV": [0.000, 1.000, 0.325, 0.450, 0.845],
            "DIG_MODE": [0, 1, 1, 0, 1],
            "DIPEER_TRIP": [0, 0, 1, 1, 0],
            "HOIST_TORQUE_INV": [0.3, 0.9, 1.0, 0.0, 0.7],
            "HOIST_IW_INV": [0.000000, 0.750000, 0.416667, 1.000000, 0.666667]
        },
        index = ["2020-01-15T13:45:30", "2020-01-15T13:45:31", "2020-01-15T13:45:32", "2020-01-15T13:45:33", "2020-01-15T13:45:34"]
    )
    assert_frame_equal(resultado, resultado_esperado, check_dtype=False, check_less_precise=True, check_like=True)
>>>>>>> Stashed changes
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49

def test_no_hay_registros_entrada_de_equipo_pesado_en_bd_entonces_retorna_lista_vacia():
    # Mock / Given
    resultado_procedimiento_almacenado = [[]]

    bd_cliente = Mock()
    bd_cliente.ejecutar_procedimiento_almacenado = MagicMock(return_value=resultado_procedimiento_almacenado)
    acceso_datos = AccesoDatos(bd_cliente)
    equipo_pesado_dummy = {
        "EQUIPO_PESADO_ID": "Shovel01"
    }

    # When
    resultado = acceso_datos.seleccionar_registro_entrada(equipo_pesado_dummy)

    # Then
    bd_cliente.ejecutar_procedimiento_almacenado.assert_called_once()
    assert resultado == []