import re


def group_class_strings(class_string, full_code):
    """Groups classes together
    Args:
        class_string: str - unprocessed string
        full_code: str - current class code (Eg. MAT 101)

    Returns:
        list[str]: list of partitioned classes for standardize_reg and hybrid to standardize
    """
    # Escape special characters in the course code for regex
    full_code = re.escape(full_code)
    
    # Regular expression to match the entire class entry
    pattern = rf'({full_code}\n.*?)\n(\d+ of \d+)(?=\n\n{full_code}|\Z)'
    matches = re.finditer(pattern, class_string, re.DOTALL)
    
    result = []
    for match in matches:
        class_info = match.group(1).strip()
        capacity = match.group(2)
        result.append(f"{class_info}\n{capacity}")
    
    return result


def standardize_reg(input_data):
    """Standardizes format for regular classes
    Args:
        input_data: one class that is unstandardized
    
    Returns:
        str: standardized format string
    """
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
    """Standardizes format for hybrid classes
    Args:
        input_data: one hybrid class that is unstandardized
    
    Returns:
        str: standardized format string
    """
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
