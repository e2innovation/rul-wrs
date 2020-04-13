import os
import pytest
import sys
from src.obtener_orquestador import ObtenerOrquestador
from src.integration.util.util_test import UtilTest

@pytest.fixture
def orquestador():
    return ObtenerOrquestador.obtener_orquestador("src\\config.json")

def test_Given_registros_para_pala_PALA_TEST01_When_monitorear_Then_los_ciclos_son_detectados_correctamente(orquestador):
    # Given
    equipo_pesado_id = 'PALA_TEST01'
    bd_cliente = orquestador.acceso_datos.bd_cliente
    UtilTest.insertar_equipo_pesado_prueba(bd_cliente.conexion, equipo_pesado_id)
    UtilTest.insertar_archivo_csv_en_tabla("src\\integration\\data\\PALA_00.csv", bd_cliente.conexion, "dbo.IOT_GATEWAY")
    
    # When
    orquestador.monitorear()
    
    # Then
    cantidad_ciclos = UtilTest.obtener_ciclos_por_equipo(bd_cliente, equipo_pesado_id)
    UtilTest.eliminar_data_prueba(bd_cliente.conexion, equipo_pesado_id)
    assert cantidad_ciclos == 6

def test_Given_registros_para_pala_PALA_TEST01_When_monitorear_es_ejecutado_muchas_veces_Then_los_ciclos_son_detectados_todas_las_veces_correctamente(orquestador):
    # Given
    equipo_pesado_id = 'PALA_TEST01'
    bd_cliente = orquestador.acceso_datos.bd_cliente
    UtilTest.insertar_equipo_pesado_prueba(bd_cliente.conexion, equipo_pesado_id)
    
    # When
    cantidad_ciclos_por_ejecucion = []
    
    # Ejecución N° 1
    UtilTest.insertar_archivo_csv_en_tabla("src\\integration\\data\\PALA_01.csv", bd_cliente.conexion, "dbo.IOT_GATEWAY")
    orquestador.monitorear()
    cantidad_ciclos = UtilTest.obtener_ciclos_por_equipo(bd_cliente, equipo_pesado_id)
    cantidad_ciclos_por_ejecucion.append(cantidad_ciclos)

    # Ejecución N° 2
    UtilTest.insertar_archivo_csv_en_tabla("src\\integration\\data\\PALA_02.csv", bd_cliente.conexion, "dbo.IOT_GATEWAY")
    orquestador.monitorear()
    cantidad_ciclos = UtilTest.obtener_ciclos_por_equipo(bd_cliente, equipo_pesado_id)
    cantidad_ciclos_por_ejecucion.append(cantidad_ciclos)

    # Ejecución N° 3
    UtilTest.insertar_archivo_csv_en_tabla("src\\integration\\data\\PALA_03.csv", bd_cliente.conexion, "dbo.IOT_GATEWAY")
    orquestador.monitorear()
    cantidad_ciclos = UtilTest.obtener_ciclos_por_equipo(bd_cliente, equipo_pesado_id)
    cantidad_ciclos_por_ejecucion.append(cantidad_ciclos)

    # Ejecución N° 4
    UtilTest.insertar_archivo_csv_en_tabla("src\\integration\\data\\PALA_04.csv", bd_cliente.conexion, "dbo.IOT_GATEWAY")
    orquestador.monitorear()
    cantidad_ciclos = UtilTest.obtener_ciclos_por_equipo(bd_cliente, equipo_pesado_id)
    cantidad_ciclos_por_ejecucion.append(cantidad_ciclos)
    
    # Then
    UtilTest.eliminar_data_prueba(bd_cliente.conexion, equipo_pesado_id)
    assert cantidad_ciclos_por_ejecucion == [22, 40, 57, 76]