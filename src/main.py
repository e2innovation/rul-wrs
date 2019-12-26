from database.database_client_factory import DatabaseClientFactory

def main(arg) : 
    try:
        database_client = DatabaseClientFactory.get_database_client()
        result = database_client.execute_stored_procedure("dbo.SP_TEST", ['param1', 'param2'])
        print('without errors')
        print(result)
        print(result[2][4].TipoExamenId)
    except Exception as err:
        print(err.args)
main(0)
