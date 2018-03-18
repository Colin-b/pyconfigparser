# pyconfigparser
Python Configuration Parser (compatible python 2/3)

Sample usage:

To read the following configuration file named `configuration.ini`:

    [section]
    mandatory_property=mandatory value

You can use the following code:

    import cfgparse

    config = cfgparse.load_config('configuration.ini')
    mandatory_value = cfgparse.get_item(config, 'section', 'mandatory_property')
    optional_value = cfgparse.get_item(config, 'section', 'optional_property', 'default_value')
