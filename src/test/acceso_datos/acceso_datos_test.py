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
                "FECHA_HORA": "2018-09-09 00:00:00.467",
                "REGISTRO": '{ "campo01": "dummy 001", "campo02": "dummy 002" }'
            },
            {
                "ID": 1000001,
                "EQUIPO_PESADO_ID": "Shovel01",
                "FECHA_HORA": "2018-09-09 00:00:01.467",
                "REGISTRO": '{ "campo01": "dummy 011", "campo02": "dummy 012" }'
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