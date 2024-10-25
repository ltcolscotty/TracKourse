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
            elif "Tempe" not in cleaned_line:
                standardized_lines[-1] += " " + cleaned_line

    return "\n".join(standardized_lines)


def standardize_hybrid(input_data):
    lines = input_data.split("\n")
    corrected_lines = []

    time_info = ""
    for i, line in enumerate(lines):
        cleaned_line = line.strip().replace("�", "")

        if not cleaned_line:
            continue

        if "Multiple dates and times" in cleaned_line or "Hybrid" in cleaned_line:
            time_info = cleaned_line.replace("Multiple dates and times", "Hybrid")
        elif "-" in cleaned_line and time_info:
            time_info += " " + cleaned_line
            corrected_lines.append(time_info)
            time_info = ""
        elif "Tempe" in cleaned_line or "Internet - Hybrid" in cleaned_line:
            continue
        else:
            corrected_lines.append(cleaned_line)

    return "\n".join(corrected_lines)
