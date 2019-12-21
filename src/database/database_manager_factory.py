from .database_manager import DatabaseManager

class DatabaseManagerFactory:
    
    @staticmethod
    def get_database_manager():
        return DatabaseManager(
            'SQL SERVER',
            'DESKTOP-Q86DM30\SQLEXPRESS',
            'Pacientes',
            'sa',
            '123456'
        )