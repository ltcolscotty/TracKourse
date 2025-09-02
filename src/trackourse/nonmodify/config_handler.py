import configparser
import os
import sys

config = configparser.ConfigParser()


def get_config_path(file_path="trackourse_config.ini"):
    """Gets the configuration math for the ini file
    Returns:
        os.path: OS path to trackourse_config.ini
    """
    config_path = ""

    if getattr(sys, "frozen", False):
        base_dir = os.path.dirname(sys.executable)
        config_path = os.path.join(base_dir, file_path)
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir, '..', '..', '..', file_path)
        config_path = os.path.abspath(config_path)

    # print(config_path)
    return config_path


def path_exists(path):
    return os.path.exists(path)


def read_config():
    """Reads configuration and puts it in a dictionary format for accessing
    Returns:
        dict: reference for constant config
            ```python
            "notif_method": notification method
            "url_year": url year for url search
            "wait_time": wait time in seconds
            "id_list": ID list
            "sender_email": sender email for gateway or notification
            "sender_password": sender email password
            "target_email": email for notifications to be sent to
            "phone_number": gateway phone number
            "carrier": phone carrier
            "dev_mode": Developer mode
            ```
    """
    config_path = get_config_path()
    print(f"Config path: {config_path}")  # Debugging line

    if not os.path.exists(config_path):
        Warning("Config_handler: Path to config does not exist")

    config.read(config_path)

    if not config.sections():
        print("No sections found in config file.")  # Debugging line

    settings = {
        "notif_method": config.get("settings", "notif_method"),
        "url_year": config.getint("settings", "url_year"),
        "wait_time": config.getint("settings", "wait_time"),
        "id_list": [
            item.strip() for item in config.get("settings", "id_list").split(",")
        ],
        "sender_email": config.get("settings", "SENDER_EMAIL"),
        "sender_password": config.get("settings", "SENDER_PASSWORD"),
        "target_email": config.get("settings", "TARGET_EMAIL"),
        "phone_number": config.get("settings", "PHONE_NUMBER"),
        "carrier": config.get("settings", "CARRIER"),
        "dev_mode": config.getboolean("settings", "dev_mode"),
    }

    return settings


def write_config(field, new_data):
    """
    Modifies settings of config file
    """
    pass


def make_url_year() -> str:
    pass

def new_config(file_name = "trackourse_config.ini"):
    """
    Creates new config file with blank information
    """
    config["settings"] = {
        'notif_method' : 'sms',
        'url_year' : make_url_year(),
        'wait_time' : '15',
        'id_list' : '',
        'SENDER_EMAIL': '',
        'SENDER_PASSWORD': '',
        'TARGET_EMAIL': '',
        'PHONE_NUMBER': '',
        'CARRIER': '',
        'dev_mode': 'False'
    }

    with open(file_name, 'w') as file:
        config.write(file)
    
    print(f"Created file in {file_name}")
