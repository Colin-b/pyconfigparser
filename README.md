# pyconfigparser
Python Configuration Parser (compatible python 2/3)

Sample usage:

    try:
        # Python 3
        from configparser import ConfigParser
    except ImportError:
        # Python 2
        from ConfigParser import ConfigParser
    import cfgparse

    config_parser = ConfigParser()
    config_file_path = 'configuration.ini'
    if not config_parser.read(config_file_path):
        raise Exception('Configuration file {0} cannot be found.'.format(config_file_path))

    my_mandatory_value = cfgparse.get_item(config_parser, 'my_section', 'my_mandatory_property')
    my_optional_value = cfgparse.get_item_default(config_parser, 'my_section', 'my_mandatory_property', 'my_default_value')
