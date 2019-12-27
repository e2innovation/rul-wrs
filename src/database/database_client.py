import pyodbc

class DatabaseClient:
    def __init__(self, driver, server, database, user, password):
        self.connection = pyodbc.connect(
            f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={user};PWD={password}"
        )

    def execute_stored_procedure(self, stored_procedure_name, parameters = []):
        cursor = self.connection.cursor()
        parameters_positions = "" if len(parameters) == 0 else f" ({','.join(['?'] * len(parameters))})"
        cursor.execute(f"{{CALL {stored_procedure_name}{parameters_positions}}}", parameters)
        result = []
        rows = cursor.fetchall()
        while rows:
            result.append(rows)
            if cursor.nextset():
                rows = cursor.fetchall()
            else:
                rows = None
        cursor.close()
        return result
        