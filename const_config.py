from nonmodify.class_info import class_info

"""
FORMAT:
class_info(subj, nbr, session, professor_list, location, start, end, honors)
"""

url_year = 2251

class_list = [
    class_info(
        "MAT",
        "267",
        session="C",
        professor_list=["Eric Kostelich", "Ryan Frier", "zdzislaw Jackwicz"],
        location="Tempe",
        start="9:00AM",
        end="5:00PM",
    ),
    class_info(
        "MAT",
        "243",
        session="C",
        professor_list=["Ajith Nair", "Haiyan Wang", "Hedvig Mohacsy"],
        location="Tempe",
        start="9:00AM",
        end="5:00PM",
    ),
    class_info(
        "ENG",
        "102",
        session="C",
        professor_list=["William Martin", "Brian Bender"],
        location="Tempe",
        start="9:00AM",
        end="5:00PM",
        id_list=["12974", "10164", "10154", "19917", "23061", "25462"],
    ),
    class_info(
        "CSE",
        "240",
        session="C",
        professor_list=["David Claveau", "James Gordon", "Justin Selgrad"],
        location="Tempe",
        start="9:00AM",
        end="5:00PM",
    ),
    class_info(
        "GRK",
        "142",
        session="C",
        professor_list=["Sarah Bolmarcich"],
        location="iCourse",
        start="9:00AM",
        end="5:00PM",
        id_list=["13837"],
    ),
]
