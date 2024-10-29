import configparser
import os
import sys


def get_config_path():
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(__file__)

    return os.path.join(base_dir, 'trackourse_config.ini')


def read_config():
    config_path = get_config_path()
    print(f"Config path: {config_path}")  # Debugging line
    config = configparser.ConfigParser()
    config.read(config_path)
    
    if not config.sections():
        print("No sections found in config file.")  # Debugging line

    settings = {
        'notif_method': config.get('settings', 'notif_method'),
        'url_year': config.getint('settings', 'url_year'),
        'wait_time': config.getint('settings', 'wait_time'),
        'id_list': [item.strip() for item in config.get('settings', 'id_list').split(',')]
    }
    
    return settings
