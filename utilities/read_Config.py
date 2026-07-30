

import configparser


def read_data(category,key):
    config = configparser.ConfigParser()
    config.read("config/config.ini")
    return config.get(category,key)
