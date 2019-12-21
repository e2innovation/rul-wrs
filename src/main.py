from database.database_manager_factory import DatabaseManagerFactory

def main(arg) : 
    database_manager = DatabaseManagerFactory.get_database_manager()
    database_manager.execute_stored_procedure("dbo.SP_COLA_X_CONSULTORIO", ('Antecedentes'))
    print('without errors')
main(0)