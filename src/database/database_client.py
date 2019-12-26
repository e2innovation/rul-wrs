import pyodbc

class DatabaseClient:
    def __init__(self, driver, server, database, user, password):
        self.connection = pyodbc.connect(
            f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={user};PWD={password}"
        )

    def execute_stored_procedure(self, stored_procedure_name, parameters):
        cursor = self.connection.cursor()
        cursor.execute(f"{{CALL {stored_procedure_name} ({','.join(['?'] * len(parameters))})}}", parameters)
        result = []
        rows = cursor.fetchall()
        while rows:
            print(rows)
            result.append(rows)
            if cursor.nextset():
                rows = cursor.fetchall()
            else:
                rows = None
        return result
        