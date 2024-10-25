def standardize_reg(input_data):
    lines = input_data.split("\n")
    standardized_lines = []

    for idx, line in enumerate(lines):
        cleaned_line = line.strip().replace("�", "")
        if cleaned_line:
            if idx == 0 or "|" in cleaned_line or "of 15" in cleaned_line:
                standardized_lines.append(cleaned_line)
            elif idx == 2:  # Instructor name
                standardized_lines.append(cleaned_line)
            elif "Tempe" not in cleaned_line:  # Skip campus and classroom info
                standardized_lines[-1] += " " + cleaned_line

    return "\n".join(standardized_lines)


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

case = """ENG 102
10155
Z�dan Xelef Almito
M W F | 12:20 PM - 1:10 PM
Tempe - WLSN112
5 of 15"""

print(case)
print("---")

# Execute the function and correct the formatting
standardized_data = standardize_reg(case)
print(standardized_data)
