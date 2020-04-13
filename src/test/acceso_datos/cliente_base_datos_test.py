import pyodbc
import pytest
from unittest.mock import Mock
from unittest.mock import MagicMock
<<<<<<< Updated upstream
from acceso_datos.cliente_base_datos import ClienteBaseDatos
=======
from src.acceso_datos.cliente_base_datos import ClienteBaseDatos
from src.test.util.row import Row
>>>>>>> Stashed changes

@pytest.fixture
def cliente_base_datos():
    driver = 'dummy_driver'
    servidor = 'dummy_servidor'
    base_datos = 'dummy_base_datos'
    usuario = 'dummy_usuario'
    contraseña = 'dummy_contraseña'
    pyodbc.connect = Mock()
    return ClienteBaseDatos(driver, servidor, base_datos, usuario, contraseña)
    
def test_conexion_correcta(cliente_base_datos):
    # Then
    pyodbc.connect.assert_called_once() 
    pyodbc.connect.assert_called_with("DRIVER={dummy_driver};SERVER=dummy_servidor;DATABASE=dummy_base_datos;UID=dummy_usuario;PWD=dummy_contraseña")

def test_conexion_fallida():
    # Given
    driver = 'dummy_driver'
    servidor = 'dummy_servidor'
    base_datos = 'dummy_base_datos'
    usuario = 'dummy_usuario'
    contraseña = 'dummy_contraseña'
    pyodbc.connect = Mock(side_effect=pyodbc.OperationalError('error code'))

    # When
    with pytest.raises(pyodbc.OperationalError) as error:
        ClienteBaseDatos(driver, servidor, base_datos, usuario, contraseña)

    # Then
    pyodbc.connect.assert_called_once() 
    pyodbc.connect.assert_called_with("DRIVER={dummy_driver};SERVER=dummy_servidor;DATABASE=dummy_base_datos;UID=dummy_usuario;PWD=dummy_contraseña")
    assert error.value.args[0] == 'error code'

def test_ejecucion_procedimiento_almacenado_sin_resultado(cliente_base_datos):
    # Given
    dummy_nombre_procedimiento_almacenado = 'dummy_procedimiento_almacenado'
    dummy_parametros = ['arg1', 'arg2', 'arg3', 'arg4']

    # Mock
    cursor = cliente_base_datos.conexion.cursor.return_value
    cursor.fetchall.return_value = None
    cursor.description = []
    
    # When
    resultado = cliente_base_datos.ejecutar_procedimiento_almacenado(dummy_nombre_procedimiento_almacenado, dummy_parametros)
    
    # Then
    cliente_base_datos.conexion.cursor.assert_called_once()
    cursor.execute.assert_called_once()
    cursor.execute.assert_called_with("{CALL dummy_procedimiento_almacenado (?,?,?,?)}", ['arg1', 'arg2', 'arg3', 'arg4'])
    cursor.fetchall.assert_called_once()
    assert resultado == [[]] # Al menos se devuelve una tabla vacia

def test_ejecucion_procedimiento_almacenado_con_varios_resultados(cliente_base_datos):
    # Given
    dummy_nombre_procedimiento_almacenado = 'dummy_procedimiento_almacenado'
    dummy_parametros = ['arg1', 'arg2', 'arg3']

    # Mock
    cursor = cliente_base_datos.conexion.cursor.return_value
<<<<<<< HEAD
=======
    cursor.description = [['id'], ['name'], ['height']]
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
    cursor.fetchall = MagicMock(side_effect=[
        [
            Row({
                'id': 1,
                'name': 'Juan',
                'height': 1.73
            }),
            Row({
                'id': 2,
                'name': 'Briggi',
                'height': 1.55
            }),
            Row({
                'id': 3,
                'name': 'Josue',
                'height': 0.90
            })
        ],
        None
    ])

    # When
    resultado = cliente_base_datos.ejecutar_procedimiento_almacenado(dummy_nombre_procedimiento_almacenado, dummy_parametros)
    
    # Then
    cliente_base_datos.conexion.cursor.assert_called_once()
    cursor.execute.assert_called_once()
    cursor.execute.assert_called_with("{CALL dummy_procedimiento_almacenado (?,?,?)}", ['arg1', 'arg2', 'arg3'])
<<<<<<< HEAD
    assert len(cursor.fetchall.mock_calls) == 4
    assert resultado == [
        {
            'id': 1,
            'name': 'Juan',
            'height': 1.73
        },
        {
            'id': 2,
            'name': 'Briggi',
            'height': 1.55
        },
        {
            'id': 3,
            'name': 'Josue',
            'height': 0.90
        }
=======
    assert len(cursor.fetchall.mock_calls) == 2
    assert resultado == [
        [
            {
                'id': 1,
                'name': 'Juan',
                'height': 1.73
            },
            {
                'id': 2,
                'name': 'Briggi',
                'height': 1.55
            },
            {
                'id': 3,
                'name': 'Josue',
                'height': 0.90
            }
        ]
>>>>>>> 4f30acdbc6afbe9b80afb7bf07f99ee29d47ee49
    ]

def test_procedimiento_almacenado_ejecucion_sin_argumentos(cliente_base_datos):
    # Given
    dummy_nombre_procedimiento_almacenado = 'dummy_procedimiento_almacenado'
    
    # Mock
    cursor = cliente_base_datos.conexion.cursor.return_value
    cursor.fetchall.return_value = None
    cursor.description = []
    
    # When
    resultado = cliente_base_datos.ejecutar_procedimiento_almacenado(dummy_nombre_procedimiento_almacenado)
    
    # Then
    cliente_base_datos.conexion.cursor.assert_called_once()
    cursor.execute.assert_called_once()
    cursor.execute.assert_called_with("{CALL dummy_procedimiento_almacenado}", [])
    cursor.fetchall.assert_called_once()
    assert resultado == [[]]  # Al menos se devuelve una tabla vacia
