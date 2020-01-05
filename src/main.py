from config_reader import ConfigReader

def main(arg) : 
    reader = ConfigReader("../config.json")
    print(reader.get_value("storage"))

main(0)
