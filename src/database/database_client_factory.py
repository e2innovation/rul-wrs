from .database_client import DatabaseClient

class DatabaseClientFactory:
    
    @staticmethod
    def get_database_client():
        return DatabaseClient(
            'SQL SERVER',
            'DESKTOP-Q86DM30\SQLEXPRESS',
            'RUL-WRS',
            'sa',
            '123456'
        )