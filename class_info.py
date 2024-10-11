from datetime import datetime


def convert_time(time_str):
    return datetime.strptime(time_str, "%I:%M%p")


class class_info:
    def __init__(
        self,
        subj: str,
        nbr: str,
        session: str,
        professor_list: list[str],
        location: str = "Tempe",
        start: str = None,
        end: str = None,
        honors: bool = False,
        required: bool = True,
        id_list: list[str] = None,
    ):
        self.subj = subj.upper()
        self.nbr = nbr
        self.session = session.upper()
        self.professor_list = professor_list
        self.location = location
        self.honors = honors
        self.fullcode = self.subj + self.nbr
        self.required = required

        if id is not None:
            self.has_id = True
            self.id = id_list
        else:
            self.has_id = False
            self.id = None

        try:
            if start is None:
                self.start = convert_time("12:01AM")
            else:
                self.start = convert_time(start)
        except ValueError:
            print(
                f"Invalid start time input {self.fullcode}, setting to default: 12:01AM"
            )
            self.start = convert_time("12:01AM")

        try:
            if start is None:
                self.end = convert_time("11:59PM")
            else:
                self.end = convert_time(start)
        except ValueError:
            print(
                f"Invalid end time input {self.fullcode}, setting to default: 11:59PM"
            )
            self.end = convert_time("11:59PM")
