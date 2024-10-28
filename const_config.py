from nonmodify.class_info import class_info

"""
This file should contain:

notif_method, url_year, wait_time, and class_list

class_info format:
    subj: Subject code (eg. [ENG] 101)
    nbr: class number (eg. ENG [101])
    session: A, B, C sessions
    professor_list: If you have any preferred professors
    location: Campus, put the code in caps. [TEMPE, DTPHX, ICOURSE, WEST VALLEY]
    start: earliest you want to go to class
    end: preferred end time if you don't want a class to go past a certain time
    honors: I'm not an honors student so this unfortunately isn't a high priority
    hybrid_allowed: Keep this as false for now, hybrid functionality will be added in the future
    iCourse_allowed: if you want to take iCourse classes
    id_list: specific class IDs you may want. These are 5 digit numbers
    days: days of the week you want; "M W", "M W F", "T Th" are common ones

"""
# Set according to method you want: [email, sms, both]
notif_method = "sms"

wait_time = 15

url_year = 2251  # configure based on current year url (eg. 2025 spring is 2551, 2557 is probably 2025 fall)

# Add or delete class entries as needed. If you have a specific hybrid course you are looking for, specify the ID, it is a feasible workaround for filtering
class_list = [
    class_info(
        "MAT",
        "267",
        professor_list=["Eric Kostelich", "Ryan Frier", "zdzislaw Jackwicz"],
        location="TEMPE",
        start="9:00AM",
        end="5:00PM",
    ),
    class_info(
        "MAT",
        "243",
        professor_list=["Ajith Nair", "Haiyan Wang", "Hedvig Mohacsy"],
        location="TEMPE",
        start="9:00AM",
        end="5:00PM",
    ),
    class_info(
        "ENG",
        "102",
        professor_list=["William Martin", "Brian Bender"],
        location="TEMPE",
        start="9:00AM",
        end="5:00PM",
        id_list=["12974", "10164", "10154", "19917", "23061", "25462"],
    ),
    class_info(
        "CSE",
        "240",
        professor_list=["David Claveau", "James Gordon", "Justin Selgrad"],
        location="TEMPE",
        start="9:00AM",
        end="5:00PM",
    ),
    class_info(
        "GRK",
        "142",
        professor_list=["Sarah Bolmarcich"],
        location="ICOURSE",
        start="9:00AM",
        end="5:00PM",
        id_list=["13837"],
    ),
]

id_list = []  # 2025 planned feature

search_method = "default"  # 2025 planned feature

# If you want to be spammed when you first run this with currently open classes
initial_update = False 
