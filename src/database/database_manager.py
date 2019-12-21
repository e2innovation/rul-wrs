import pyodbc

class DatabaseManager:
    def __init__(self, driver, server, database, user, password):
        self.connection = pyodbc.connect(
            f"DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password}"
        )

    def execute_stored_procedure(self, stored_procedure, parameters):
        #self.connection.execute(f"{CALL usp_UpdateFirstName ({','.join(['?'] * len(parameters))})}", parameters)
        pass