from trackourse.nonmodify.config_handler import read_config

settings = read_config()

notif_method = settings["notif_method"]
url_year = settings["url_year"]
wait_time = settings["wait_time"]
id_list = settings["id_list"]
