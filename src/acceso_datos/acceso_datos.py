from util.estado_equipo_pesado import EstadoEquipoPesado

class AccesoDatos:
    def __init__(self, bd_cliente):
        self.bd_cliente = bd_cliente

    def seleccionar_equipos_pesados(self):
        resultado = self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.SELECCIONAR_EQUIPO_PESADO")
        equipos_pesados = resultado[0] if len(resultado) > 0 else []
        return [equipo_pesado for equipo_pesado in equipos_pesados if equipo_pesado.ESTADO == EstadoEquipoPesado.FUNCIONANDO.value]

    def cambiar_estado_equipo_pesado(self, equipo_pesado, estado):
        self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.CAMBIAR_ESTADO_EQUIPO_PESADO", [equipo_pesado.EQUIPO_PESADO_ID, estado.value])

    def seleccionar_registro_entrada(self, equipo_pesado):
        resultado = self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.SELECCIONAR_REGISTRO_ENTRADA", [equipo_pesado.EQUIPO_PESADO_ID])
        registros_entrada = resultado[0] if len(resultado) > 0 else []
        return registros_entrada

    def crear_ciclo(self, equipo_pesado, registros):
        # Crear el estado de ciclo
        # Crear un bucle que itere y vaya insertando los registros
        resultado = self.bd_cliente.ejecutar_procedimiento_almacenado("dbo.CREAR_CICLO", [equipo_pesado.EQUIPO_PESADO_ID, ''])
        ciclos = resultado[0] if len(resultado) > 0 else []
        return ciclos[0]

        



