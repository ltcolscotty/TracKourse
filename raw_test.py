import re


def group_class_strings(class_string, full_code):
    # Escape special characters in the course code for regex
    full_code = re.escape(full_code)

    # Regular expression to match the entire class entry
    pattern = rf"({full_code}\n.*?)\n(\d+ of \d+)(?=\n\n{full_code}|\Z)"
    matches = re.finditer(pattern, class_string, re.DOTALL)

    result = []
    for match in matches:
        class_info = match.group(1).strip()
        capacity = match.group(2)
        result.append(f"{class_info}\n{capacity}")

    return result


# Test input for debugging
input_data = """
ENG 102
10148
Richard Hart
T Th | 1:30 PM - 2:45 PM
Tempe - DISCVRY113
1 of 15

ENG 102
10152
Dana Tait
Multiple dates and times | 9:00 AM

� - 10:15 AM

�
Tempe - EDB120

Internet - Hybrid
8 of 15

ENG 102
10155
Z�dan Xelef Almito
M W F | 12:20 PM - 1:10 PM
Tempe - WLSN112
5 of 15

ENG 102
10162
Jennifer Waters
Multiple dates and times | 3:00 PM

� - 4:15 PM

�
Tempe - COORL1-84

Internet - Hybrid
10 of 15

ENG 102
10163
Emre Kahveci
T Th | 3:00 PM - 4:15 PM
Tempe - CRTVC207
13 of 15
"""

# Execute the function and correct the formatting
standardized_data = group_class_strings(input_data, "ENG 102")
for i in standardized_data:
    print("---")
    print(i)
    print("---")
