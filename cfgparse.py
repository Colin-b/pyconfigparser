try:
    # Python 3
    from configparser import ConfigParser
except ImportError:
    # Python 2
    from ConfigParser import ConfigParser
    
def load_config(file_path):
    """
    Load configuration parser from ini file.
    Throw an Exception if file cannot be found.
    
    :param file_path: string path to the configuration ini file.
    :return: ConfigParser instance.
    """
    config_parser = ConfigParser()
    if not config_parser.read(file_path):
        raise Exception('Configuration file "{0}" cannot be found.'.format(file_path))
    return config_parser


def get_item(config, section, key, *args):
    """
    Return property value or throw an Exception if it cannot be found and no default value is provided.
    
    :param config: Configuration parser instance.
    :param section: Section name in configuration with property to look for.
    :param key: Name of the key to look for in section.
    :param args: Can contains the default value (consider as mandatory if nothing is provided).
    :return: Key string value.
    """
    try:
        # Python 3
        section_dict = config[section]
        if key not in section_dict and not args:
            raise Exception('"{0}" configuration section must provide "{1}".'.format(section, key))
        return section_dict[key] if key in section_dict else args[0]
    except AttributeError:
        # Python 2
        if not config.has_option(section, key) and not args:
            raise Exception('"{0}" configuration section must provide "{1}".'.format(section, key))
        return config.get(section, key) if config.has_option(section, key) else args[0]
