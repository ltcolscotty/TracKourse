import configparser
import os
import sys


def get_config_path():
    """Gets the configuration math for the ini file
    Returns:
        os.path: OS path to trackourse_config.ini
    """
    if getattr(sys, "frozen", False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(__file__)

    return os.path.join(base_dir, "trackourse_config.ini")


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
    config = configparser.ConfigParser()
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
