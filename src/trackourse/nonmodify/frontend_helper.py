import trackourse.nonmodify.web_info as wi
import trackourse.nonmodify.config_handler as ch


def verify_class(id: str) -> bool:
    """
    Search to make sure class ID Exists

    Args:
        - id - class ID

    Returns:
        - Bool - Whether class exists or not
    """
    pass


def get_current_classes():
    settings_list = ch.read_config()
    return settings_list["id_list"]


def add_class(id: str):
    """
    Adds class to INI file
    """
    url = wi.url_from_id(id)
    ch.write_config("id_list", id)


def remove_class(id: str):
    """
    Removes class from ini file if it exists
    """
    pass


def start_notifier():
    pass


def stop_notifier():
    pass
