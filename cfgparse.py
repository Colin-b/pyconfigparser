try:
    # Python 3
    from configparser import ConfigParser
except ImportError:
    # Python 2
    from ConfigParser import ConfigParser
    
def load_config(file_path):
    """
    Load configuration parser from ini file.
    
    :param file_path: string path to the configuration ini file.
    :return: ConfigParser instance.
    :raise Exception: If file cannot be found
    """
    config_parser = ConfigParser()
    if not config_parser.read(file_path):
        raise Exception('Configuration file "{0}" cannot be found.'.format(file_path))
    return config_parser


def get_item(config, section, key, *args):
    """
    Return property value.
    
    :param config: Configuration parser instance.
    :param section: Section name in configuration with property to look for.
    :param key: Name of the key to look for in section.
    :param args: Can contains the default value (consider as mandatory if nothing is provided).
    :return: Key string value.
    :raise Exception: If key cannot be found and not default value is provided.
    """
    if not config.has_option(section, key) and not args:
        raise Exception('"{0}" configuration section must provide "{1}".'.format(section, key))
    return config.get(section, key) if config.has_option(section, key) else args[0]
