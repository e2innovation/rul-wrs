class Storage:
    def __init__(self, database_client):
        self.database_client = database_client

    def get_machine(self):
        query_result = self.database_client.execute_stored_procedure("dbo.MACHINE_SELECT")
        machines = query_result[0]
        return [machine for machine in machines if machine.ESTADO == True]

    def get_input_records(self, machine):
        query_result = self.database_client.execute_stored_procedure("dbo.INPUT_RECORD_SELECT", [machine.MACHINE_ID])
        return query_result[0]

    def turn_off_machine(self, machine):
        self.database_client.execute_stored_procedure("dbo.TURN_OFF_MACHINE", [machine.MACHINE_ID])