import pyodbc

class DatabaseManager:
    def __init__(self, driver, server, database, user, password):
        self.connection = pyodbc.connect(
            f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={user};PWD={password}"
        )

    def execute_sp_without_result(self, stored_procedure, parameters):
        self.connection.execute(f"{{CALL {stored_procedure} ({','.join(['?'] * len(parameters))})}}", parameters)
    