from .database_client_factory import DatabaseClientFactory

class Storage:
    def __init__(self):
        self.database_client = DatabaseClientFactory.get_database_client()

    def get_enabled_machines(self):
        query_result = self.database_client.execute_stored_procedure("dbo.MACHINE_SELECT")
        machines = query_result[0]
        return [machine for machine in machines if machine.disabled == False]