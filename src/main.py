from config_reader import ConfigReader
from database.storage import Storage
from database.database_client import DatabaseClient

def main(arg) : 
    reader = ConfigReader("../config.json")
    config = reader.get_value("storage")
    client = DatabaseClient(
            config["driver"],
            config["server"],
            config["database"],
            config["user"],
            config["password"]
        )
    storage = Storage(client)
    print(storage.get_enabled_machines())

main(0)
