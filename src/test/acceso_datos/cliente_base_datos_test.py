import pyodbc
import pytest
from unittest.mock import Mock
from unittest.mock import MagicMock
from acceso_datos.cliente_base_datos import ClienteBaseDatos

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

def test_ejecucion_procedimient_almacenado_sin_resultado(cliente_base_datos):
    # Given
    dummy_stored_procedure_name = 'dummy_stored_procedure'
    dummy_parameters = ['arg1', 'arg2', 'arg3', 'arg4']

    # Mock
    cursor = cliente_base_datos.connection.cursor.return_value
    cursor.fetchall.return_value = None
    
    # When
    result = cliente_base_datos.execute_stored_procedure(dummy_stored_procedure_name, dummy_parameters)
    
    # Then
    cliente_base_datos.connection.cursor.assert_called_once()
    cursor.execute.assert_called_once()
    cursor.execute.assert_called_with("{CALL dummy_stored_procedure (?,?,?,?)}", ['arg1', 'arg2', 'arg3', 'arg4'])
    cursor.fetchall.assert_called_once()
    assert result == []

def test_stored_procedure_execution_with_many_results(cliente_base_datos):
    # Given
    dummy_stored_procedure_name = 'dummy_stored_procedure'
    dummy_parameters = ['arg1', 'arg2', 'arg3']

    # Mock
    cursor = cliente_base_datos.connection.cursor.return_value
    cursor.fetchall = MagicMock(side_effect=[
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
        },
        None
    ])

    # When
    result = cliente_base_datos.execute_stored_procedure(dummy_stored_procedure_name, dummy_parameters)
    
    # Then
    cliente_base_datos.connection.cursor.assert_called_once()
    cursor.execute.assert_called_once()
    cursor.execute.assert_called_with("{CALL dummy_stored_procedure (?,?,?)}", ['arg1', 'arg2', 'arg3'])
    assert len(cursor.fetchall.mock_calls) == 4
    assert result == [
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

def test_stored_procedure_execution_without_arguments(cliente_base_datos):
    # Given
    dummy_stored_procedure_name = 'dummy_stored_procedure'
    
    # Mock
    cursor = cliente_base_datos.connection.cursor.return_value
    cursor.fetchall.return_value = None
    
    # When
    result = cliente_base_datos.execute_stored_procedure(dummy_stored_procedure_name)
    
    # Then
    cliente_base_datos.connection.cursor.assert_called_once()
    cursor.execute.assert_called_once()
    cursor.execute.assert_called_with("{CALL dummy_stored_procedure}", [])
    cursor.fetchall.assert_called_once()
    assert result == []