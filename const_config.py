from nonmodify.class_info import class_info

"""
FORMAT:
class_info(subj, nbr, session, professor_list, location, start, end, honors)
"""

class_list = [
    class_info(
        "MAT",
        "267",
        "C",
        ["Eric Kostelich", "Ryan Frier", "zdzislaw Jackwicz"],
        "Tempe",
        "9:00AM",
        "5:00PM",
    ),
    class_info(
        "MAT",
        "243",
        "C",
        ["Ajitg Nair", "Haiyan Wang", "Hedvig Mohacsy"],
        "Tempe",
        "9:00AM",
        "5:00PM",
    ),
    class_info(
        "ENG",
        "102",
        "C",
        ["William Martin", "Brian Bender"],
        "Tempe",
        "9:00AM",
        "5:00PM",
        id_list=["12974", "10164", "10154", "19917", "23061", "25462"],
    ),
    class_info(
        "CSE",
        "240",
        "C",
        ["David Claveau", "James Gordon", "Justin Selgrad"],
        "Tempe",
        "9:00AM",
        "5:00PM",
    ),
    class_info(
        "PHI",
        "105",
        "C",
        ["Douglas Portmore"],
        "Tempe",
        "9:00AM",
        "5:00PM",
        id_list=["12551"],
    ),
    class_info(
        "CON",
        "101",
        "C",
        ["Anthony Lamanna"],
        "Tempe",
        "9:00AM",
        "5:00PM",
        id_list=["11027"],
    ),
    class_info(
        "GRK",
        "142",
        "C",
        ["Sarah Bolmarcich"],
        "iCourse",
        "9:00AM",
        "5:00PM",
        id_list=["13837"],
    ),
]
