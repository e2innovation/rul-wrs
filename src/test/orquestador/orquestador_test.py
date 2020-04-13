import pytest
from unittest.mock import Mock
from unittest.mock import MagicMock
from orquestador.orquestador import Orquestador
from util.estado_equipo_pesado import EstadoEquipoPesado

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
            "ESTADO": EstadoEquipoPesado.FUNCIONANDO,
            "REPORTE": '{ "contenido": "contenido dummy 01" }'
        },
        {
            "EQUIPO_PESADO_ID": "Shovel02",
            "TIPO": "Shovel",
            "DESCRIPCION": "dummy descripción 02",
            "ESTADO": EstadoEquipoPesado.APAGADO,
            "REPORTE": '{ "contenido": "contenido dummy 02" }'
        },
        {
            "EQUIPO_PESADO_ID": "Shovel03",
            "TIPO": "Shovel",
            "DESCRIPCION": "dummy descripción 03",
            "ESTADO": EstadoEquipoPesado.FUNCIONANDO,
            "REPORTE": '{ "contenido": "contenido dummy 03" }'
        },
        {
            "EQUIPO_PESADO_ID": "Shovel04",
            "TIPO": "Shovel",
            "DESCRIPCION": "dummy descripción 04",
            "ESTADO": EstadoEquipoPesado.APAGADO,
            "REPORTE": '{ "contenido": "contenido dummy 04" }'
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
            { "campo01": "valor13", "campo02": "valor14", "campo03": "valor15" }
        ],
        [
            { "campo01": "valor16", "campo02": "valor17", "campo03": "valor18" },
            { "campo01": "valor19", "campo02": "valor20", "campo03": "valor21" }
        ],
        []
    ]

def test_prender_equipo_pesado_apagado_cuando_se_detecta_actividad(orquestador, equipos_pesados):
    # Mock / Given
<<<<<<< HEAD
=======
<<<<<<< Updated upstream
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
    orquestador.acceso_datos.seleccionar_equipos_pesados = MagicMock(return_value = equipos_pesados)
    orquestador.detector_ciclos.es_ciclo = Mock(side_effect = [
        (False, EstadoEquipoPesado.FUNCIONANDO),
        (False, EstadoEquipoPesado.FUNCIONANDO), # Este se prendió
        (False, EstadoEquipoPesado.FUNCIONANDO),
        (False, EstadoEquipoPesado.APAGADO)
    ])
<<<<<<< HEAD
=======
=======
    orquestador.acceso_datos.seleccionar_equipos_pesados_activos = MagicMock(return_value = equipos_pesados)
    orquestador.acceso_datos.seleccionar_registros_entrada = MagicMock(return_value = registros_entrada)
    orquestador.detector_ciclos.detectar_ciclos = Mock(side_effect = ciclos)
>>>>>>> Stashed changes
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49

    # When
    orquestador.monitorear()

    # Then
<<<<<<< HEAD
=======
<<<<<<< Updated upstream
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
    assert(orquestador.detector_ciclos.seleccionar_registro_entrada.call_count, 4)
    assert(orquestador.detector_ciclos.es_ciclo.call_count, 4)
    orquestador.acceso_datos.cambiar_estado_equipo_pesado.assert_called_once_with(
        {
            "EQUIPO_PESADO_ID": "Shovel02",
            "TIPO": "Shovel",
            "DESCRIPCION": "dummy descripción 02",
            "ESTADO": EstadoEquipoPesado.APAGADO,
            "REPORTE": '{ "contenido": "contenido dummy 02" }'
        },
        EstadoEquipoPesado.FUNCIONANDO
    )
<<<<<<< HEAD

def test_apagar_equipo_pesado_funcionando_cuando_no_se_detecta_actividad(orquestador, equipos_pesados):
    # Mock / Given
=======
=======
    assert(orquestador.acceso_datos.seleccionar_equipos_pesados_activos.call_count == 1)
    assert(orquestador.acceso_datos.guardar_ciclo.call_count == 5)
    orquestador.acceso_datos.guardar_ciclo.assert_has_calls([
        call({ "CICLO_ID": "ciclo1" }),
        call({ "CICLO_ID": "ciclo2" }),
        call({ "CICLO_ID": "ciclo3" }),
        call({ "CICLO_ID": "ciclo4" }),
        call({ "CICLO_ID": "ciclo5" })
    ])

>>>>>>> Stashed changes

def test_apagar_equipo_pesado_funcionando_cuando_no_se_detecta_actividad(orquestador, equipos_pesados):
    # Mock / Given
<<<<<<< Updated upstream
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
    orquestador.acceso_datos.seleccionar_equipos_pesados = MagicMock(return_value = equipos_pesados)
    orquestador.detector_ciclos.es_ciclo = Mock(side_effect = [
        (False, EstadoEquipoPesado.FUNCIONANDO),
        (False, EstadoEquipoPesado.APAGADO),
        (False, EstadoEquipoPesado.APAGADO), # Este se apagó
        (False, EstadoEquipoPesado.APAGADO)
    ])
<<<<<<< HEAD
=======
=======
    orquestador.acceso_datos.seleccionar_equipos_pesados_activos = MagicMock(return_value = [])
>>>>>>> Stashed changes
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49

    # When
    orquestador.monitorear()

    # Then
<<<<<<< HEAD
=======
<<<<<<< Updated upstream
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
    assert(orquestador.detector_ciclos.seleccionar_registro_entrada.call_count, 4)
    assert(orquestador.detector_ciclos.es_ciclo.call_count, 4)
    orquestador.acceso_datos.cambiar_estado_equipo_pesado.assert_called_once_with(
        {
            "EQUIPO_PESADO_ID": "Shovel03",
            "TIPO": "Shovel",
            "DESCRIPCION": "dummy descripción 03",
            "ESTADO": EstadoEquipoPesado.FUNCIONANDO,
            "REPORTE": '{ "contenido": "contenido dummy 03" }'
        },
        EstadoEquipoPesado.APAGADO
    )
<<<<<<< HEAD

def test_crear_ciclo_y_procesar_registros_cuando_se_detecta_nuevo_ciclo(orquestador, equipos_pesados, registros_entrada):
    # Mock / Given
=======
=======
    assert(orquestador.acceso_datos.seleccionar_equipos_pesados_activos.call_count == 1)
    assert(orquestador.detector_ciclos.seleccionar_registro_entrada.call_count == 0)
    assert(orquestador.detector_ciclos.detectar_ciclos.call_count == 0)
    assert(orquestador.acceso_datos.guardar_ciclo.call_count == 0)

>>>>>>> Stashed changes

def test_crear_ciclo_y_procesar_registros_cuando_se_detecta_nuevo_ciclo(orquestador, equipos_pesados, registros_entrada):
    # Mock / Given
<<<<<<< Updated upstream
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
    orquestador.acceso_datos.seleccionar_equipos_pesados = MagicMock(return_value = equipos_pesados)
    orquestador.acceso_datos.seleccionar_registro_entrada = Mock(side_effect = registros_entrada)
    orquestador.detector_ciclos.es_ciclo = Mock(side_effect = [
        (True, EstadoEquipoPesado.FUNCIONANDO), # Se detectó un ciclo
        (False, EstadoEquipoPesado.APAGADO),
        (False, EstadoEquipoPesado.FUNCIONANDO),
        (False, EstadoEquipoPesado.APAGADO)
    ])
    orquestador.acceso_datos.crear_ciclo = MagicMock(return_value={
        "CICLO_ID": "CICLO01",
        "EQUIPO_PESADO_ID": "Shovel01",
        "ESTADO": "dummy"
    })
    orquestador.preprocesador.obtener_caracteristicas = MagicMock(return_value = [
      { "A": "caracteristica01", "B": "caracteristica02", "C": "caracteristica03" },
      { "A": "caracteristica04", "B": "caracteristica05", "C": "caracteristica06" },
      { "A": "caracteristica07", "B": "caracteristica08", "C": "caracteristica09" },
      { "A": "caracteristica10", "B": "caracteristica11", "C": "caracteristica12" },
      { "A": "caracteristica13", "B": "caracteristica14", "C": "caracteristica15" }  
    ])
<<<<<<< HEAD
=======
=======
    orquestador.acceso_datos.seleccionar_equipos_pesados_activos = MagicMock(return_value = equipos_pesados)
    orquestador.acceso_datos.seleccionar_registros_entrada = MagicMock(return_value = registros_entrada)
    orquestador.detector_ciclos.detectar_ciclos = Mock(side_effect = [[],[]])
>>>>>>> Stashed changes
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49

    # When
    orquestador.monitorear()

    # Then
<<<<<<< HEAD
=======
<<<<<<< Updated upstream
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
    assert(orquestador.detector_ciclos.seleccionar_registro_entrada.call_count, 4)
    assert(orquestador.detector_ciclos.es_ciclo.call_count, 4)
    registros_esperados = [
        { "campo01": "valor01", "campo02": "valor02", "campo03": "valor03" },
        { "campo01": "valor04", "campo02": "valor05", "campo03": "valor06" },
        { "campo01": "valor07", "campo02": "valor08", "campo03": "valor09" }
    ]
    orquestador.acceso_datos.crear_ciclo.assert_called_once_with(
        {
            "EQUIPO_PESADO_ID": "Shovel01",
            "TIPO": "Shovel",
            "DESCRIPCION": "dummy descripción 01",
            "ESTADO": EstadoEquipoPesado.FUNCIONANDO,
            "REPORTE": '{ "contenido": "contenido dummy 01" }'
        },
        registros_esperados
    )
    orquestador.preprocesador.obtener_caracteristicas.assert_called_once_with(registros_esperados)
    orquestador.acceso_datos.guardar_caracteristicas.assert_called_once_with(
        {
            "CICLO_ID": "CICLO01",
            "EQUIPO_PESADO_ID": "Shovel01",
            "ESTADO": "dummy"
        },
        [
            { "A": "caracteristica01", "B": "caracteristica02", "C": "caracteristica03" },
            { "A": "caracteristica04", "B": "caracteristica05", "C": "caracteristica06" },
            { "A": "caracteristica07", "B": "caracteristica08", "C": "caracteristica09" },
            { "A": "caracteristica10", "B": "caracteristica11", "C": "caracteristica12" },
            { "A": "caracteristica13", "B": "caracteristica14", "C": "caracteristica15" }  
        ]
<<<<<<< HEAD
    )
=======
    )
=======
    assert(orquestador.acceso_datos.seleccionar_equipos_pesados_activos.call_count == 1)
    assert(orquestador.detector_ciclos.detectar_ciclos.call_count == 2)
    assert(orquestador.acceso_datos.guardar_ciclo.call_count == 0)


>>>>>>> Stashed changes
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
