import pytest
from unittest.mock import Mock, MagicMock, call
from src.orquestador.orquestador import Orquestador
from src.util.estado_equipo_pesado import EstadoEquipoPesado

@pytest.fixture
def orquestador():
    return Orquestador(
        acceso_datos = Mock(),
        detector_ciclos = Mock(),
        preprocesador = Mock(),
        clasificador = Mock(),
        predictor = Mock()
    )

@pytest.fixture
def equipos_pesados():
    return [
        {
            "EQUIPO_PESADO_ID": "Shovel01",
            "TIPO": "Shovel",
            "DESCRIPCION": "dummy descripción 01",
            "ESTADO": EstadoEquipoPesado.HABILITADO,
            "REPORTE": '{ "contenido": "contenido dummy 01" }'
        },
        {
            "EQUIPO_PESADO_ID": "Shovel03",
            "TIPO": "Shovel",
            "DESCRIPCION": "dummy descripción 03",
            "ESTADO": EstadoEquipoPesado.HABILITADO,
            "REPORTE": '{ "contenido": "contenido dummy 03" }'
        }
    ]

@pytest.fixture
def registros_entrada():
    return [
        [
            { "campo01": "valor01", "campo02": "valor02", "campo03": "valor03" },
            { "campo01": "valor04", "campo02": "valor05", "campo03": "valor06" },
            { "campo01": "valor07", "campo02": "valor08", "campo03": "valor09" }
        ],
        [
            { "campo01": "valor10", "campo02": "valor11", "campo03": "valor12" },
            { "campo01": "valor13", "campo02": "valor14", "campo03": "valor15" },
            { "campo01": "valor16", "campo02": "valor17", "campo03": "valor18" },
            { "campo01": "valor19", "campo02": "valor20", "campo03": "valor21" }
        ],
    ]

@pytest.fixture
def ciclos():
    return [
        [{ "CICLO_ID": "ciclo1" }, { "CICLO_ID": "ciclo2" }, { "CICLO_ID": "ciclo3" }],
        [{ "CICLO_ID": "ciclo4" }, { "CICLO_ID": "ciclo5" }]
    ]

def test_Given_equipos_habilitados_When_monitorar_es_ejecutado_Then_extrae_y_guarda_ciclos_detectados(
    orquestador, 
    equipos_pesados,
    registros_entrada,
    ciclos
):
    # Mock / Given
    orquestador.acceso_datos.seleccionar_equipos_pesados_activos = MagicMock(return_value = equipos_pesados)
    orquestador.acceso_datos.seleccionar_registros_entrada = MagicMock(return_value = registros_entrada)
    orquestador.detector_ciclos.detectar_ciclos = Mock(side_effect = ciclos)

    # When
    orquestador.monitorear()

    # Then
    assert(orquestador.acceso_datos.seleccionar_equipos_pesados_activos.call_count == 1)
    assert(orquestador.acceso_datos.guardar_ciclo.call_count == 5)
    orquestador.acceso_datos.guardar_ciclo.assert_has_calls([
        call({ "CICLO_ID": "ciclo1" }),
        call({ "CICLO_ID": "ciclo2" }),
        call({ "CICLO_ID": "ciclo3" }),
        call({ "CICLO_ID": "ciclo4" }),
        call({ "CICLO_ID": "ciclo5" })
    ])


def test_Given_ningun_equipo_pesado_habilitado_When_monitorear_Then_ningun_registro_procesado_o_ciclo_detectado(orquestador):
    # Mock / Given
    orquestador.acceso_datos.seleccionar_equipos_pesados_activos = MagicMock(return_value = [])

    # When
    orquestador.monitorear()

    # Then
    assert(orquestador.acceso_datos.seleccionar_equipos_pesados_activos.call_count == 1)
    assert(orquestador.detector_ciclos.seleccionar_registro_entrada.call_count == 0)
    assert(orquestador.detector_ciclos.detectar_ciclos.call_count == 0)
    assert(orquestador.acceso_datos.guardar_ciclo.call_count == 0)


def test_Given_equipos_pesados_habilitados_sin_ciclos_detectados_When_monitorear_Then_ningun_ciclo_creado(
    orquestador,
    equipos_pesados,
    registros_entrada
):
    # Mock / Given
    orquestador.acceso_datos.seleccionar_equipos_pesados_activos = MagicMock(return_value = equipos_pesados)
    orquestador.acceso_datos.seleccionar_registros_entrada = MagicMock(return_value = registros_entrada)
    orquestador.detector_ciclos.detectar_ciclos = Mock(side_effect = [[],[]])

    # When
    orquestador.monitorear()

    # Then
    assert(orquestador.acceso_datos.seleccionar_equipos_pesados_activos.call_count == 1)
    assert(orquestador.detector_ciclos.detectar_ciclos.call_count == 2)
    assert(orquestador.acceso_datos.guardar_ciclo.call_count == 0)


