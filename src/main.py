from database.storage import Storage

def main(arg) : 
    storage = Storage()
    print(storage.get_enabled_machines())

main(0)
