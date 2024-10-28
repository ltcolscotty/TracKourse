from nonmodify.class_info import class_info

"""
This file should contain:

notif_method, url_year, wait_time, and class_list

class_info format:
    subj: Subject code (eg. [ENG] 101)
    nbr: class number (eg. ENG [101])
    session: A, B, C sessions
    professor_list: If you have any preferred professors
    location: Campus, put the code in caps. [TEMPE, DTPHX, ICOURSE, POLY]
    start: earliest you want to go to class
    end: preferred end time if you don't want a class to go past a certain time
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
        "243",
        professor_list=["Ajith Nair", "Haiyan Wang", "Hedvig Mohacsy"],
        location="TEMPE",
        start="9:00AM",
        end="5:00PM",
        id_list=['12275'],
    ),
]

id_list = []  # 2025 planned feature

# Options: class_list, id_list
search_method = "class_list"  # 2025 planned feature
