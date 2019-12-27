import pyodbc
import pytest
from unittest.mock import Mock
from unittest.mock import MagicMock
from database.database_client import DatabaseClient

@pytest.fixture
def database_client():
    driver = 'dummy_driver'
    server = 'dummy_server'
    database = 'dummy_database'
    user = 'dummy_user'
    password = 'dummy_password'
    pyodbc.connect = Mock()
    return DatabaseClient(driver, server, database, user, password)
    
def test_right_connection(database_client):
    # Then
    pyodbc.connect.assert_called_once() 
    pyodbc.connect.assert_called_with("DRIVER={dummy_driver};SERVER=dummy_server;DATABASE=dummy_database;UID=dummy_user;PWD=dummy_password")

def test_fail_connection():
    # Given
    driver = 'dummy_driver'
    server = 'dummy_server'
    database = 'dummy_database'
    user = 'dummy_user'
    password = 'dummy_password'
    pyodbc.connect = Mock(side_effect=pyodbc.OperationalError('error code'))

    # When
    with pytest.raises(pyodbc.OperationalError) as error:
        DatabaseClient(driver, server, database, user, password)

    # Then
    pyodbc.connect.assert_called_once() 
    pyodbc.connect.assert_called_with("DRIVER={dummy_driver};SERVER=dummy_server;DATABASE=dummy_database;UID=dummy_user;PWD=dummy_password")
    assert error.value.args[0] == 'error code'

def test_stored_procedure_execution_without_result(database_client):
    # Given
    dummy_stored_procedure_name = 'dummy_stored_procedure'
    dummy_parameters = ['arg1', 'arg2', 'arg3', 'arg4']

    # Mock
    cursor = database_client.connection.cursor.return_value
    cursor.fetchall.return_value = None
    
    # When
    result = database_client.execute_stored_procedure(dummy_stored_procedure_name, dummy_parameters)
    
    # Then
    database_client.connection.cursor.assert_called_once()
    cursor.execute.assert_called_once()
    cursor.execute.assert_called_with("{CALL dummy_stored_procedure (?,?,?,?)}", ['arg1', 'arg2', 'arg3', 'arg4'])
    cursor.fetchall.assert_called_once()
    assert result == []

def test_stored_procedure_execution_with_many_results(database_client):
    # Given
    dummy_stored_procedure_name = 'dummy_stored_procedure'
    dummy_parameters = ['arg1', 'arg2', 'arg3']

    # Mock
    cursor = database_client.connection.cursor.return_value
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
    result = database_client.execute_stored_procedure(dummy_stored_procedure_name, dummy_parameters)
    
    # Then
    database_client.connection.cursor.assert_called_once()
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

def test_stored_procedure_execution_without_arguments(database_client):
    # Given
    dummy_stored_procedure_name = 'dummy_stored_procedure'
    
    # Mock
    cursor = database_client.connection.cursor.return_value
    cursor.fetchall.return_value = None
    
    # When
    result = database_client.execute_stored_procedure(dummy_stored_procedure_name)
    
    # Then
    database_client.connection.cursor.assert_called_once()
    cursor.execute.assert_called_once()
    cursor.execute.assert_called_with("{CALL dummy_stored_procedure}", [])
    cursor.fetchall.assert_called_once()
    assert result == []