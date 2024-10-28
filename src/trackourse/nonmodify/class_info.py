"""
if ID is not entered in, all options should be scanned
"""

from datetime import datetime


def convert_time(time_str):
    return datetime.strptime(time_str, "%I:%M%p")


class class_info:
    def __init__(
        self,
        subj: str,
        nbr: str,
        session: str = "C",
        professor_list: list[str] = [],
        location: str = "TEMPE",
        start: str = None,
        end: str = None,
        id_list: list[str] = None,
        days: list[str] = ["M W F", "T Th", "M W", "M", "T", "W", "Th", "F"],
    ):
        self.subj = subj.upper()
        self.nbr = nbr
        self.session = session.upper()
        self.professor_list = professor_list
        self.location = location.upper()
        self.fullcode = f"{self.subj} {self.nbr}"
        self.days = days

        if id is not None:
            self.has_id = True
            self.id = id_list
        else:
            self.has_id = False
            self.id = []

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
                self.end = convert_time(end)
        except ValueError:
            print(
                f"Invalid end time input {self.fullcode}, setting to default: 11:59PM"
            )
            self.end = convert_time("11:59PM")
