import configparser

CONFIG_FILE = "bastion_config.ini"


def get_config_section_values(section, val):
    """Returns the requested values"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config.get(section, val)
