import re
from datetime import datetime

from trackourse.nonmodify.class_info import class_info as ci


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
    pattern = rf"({full_code}\n.*?)\n(\d+ of \d+)(?=\n\n{full_code}|\Z)"
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
            if idx == 0 or idx == 1:
                standardized_lines.append(cleaned_line)
            elif idx == 2:
                standardized_lines.append(cleaned_line)
            elif "|" in cleaned_line:
                standardized_lines.append(cleaned_line)
            elif "of 15" in cleaned_line:
                standardized_lines.append(cleaned_line)

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
            time_info += cleaned_line
            corrected_lines.append(time_info)
            time_info = ""
        elif "Tempe" in cleaned_line or "Internet - Hybrid" in cleaned_line:
            continue
        else:
            corrected_lines.append(cleaned_line)

    return "\n".join(corrected_lines)


def is_not_hybrid(course_input):
    """Checks if entry is a hybrid class or not for processing
    Args:
        course_input: str - one course information

    Returns:
        bool: true if course is a regular course
    """
    lines = course_input.split("\n")

    # Check if the entry has at least 6 lines (non-hybrid entries have exactly 6 lines)
    if len(lines) != 6:
        return False

    time_pattern = (
        r"^[MTWRFS]+\s+\|\s+\d{1,2}:\d{2}\s+[AP]M\s+-\s+\d{1,2}:\d{2}\s+[AP]M$"
    )
    if not re.match(time_pattern, lines[3].strip()):
        return False

    # Check if the location doesn't contain "Internet - Hybrid"
    if "Internet - Hybrid" in lines[4]:
        return False

    # If all checks pass, it's a non-hybrid course
    return True


def standardize(input, class_info: ci):
    """Standardizes total input
    Args:
        input: str - raw preprocessed input
        class_info: nonmodify.class_info.class_info - current class selection
    Returns:
        list[str]: Standardized info
    """
    info_list = group_class_strings(input, class_info.fullcode)
    print(class_info.fullcode)
    for i, course in enumerate(info_list):
        if is_not_hybrid(course):
            info_list[i] = standardize_reg(course)
        else:
            info_list[i] = standardize_hybrid(course)

    return info_list


def process_class(input_string):
    lines = input_string.strip().split("\n")

    if len(lines) != 5:
        raise ValueError("Input must contain exactly 5 lines.")

    course = lines[0].strip()
    course_id = lines[1].strip()
    instructor = lines[2].strip()
    schedule_line = lines[3].strip()
    capacity_line = lines[4].strip()

    if "Hybrid" in schedule_line:
        days = "Hybrid"
        time_info = schedule_line.split("|")[1].strip()
    else:
        days, time_info = schedule_line.split("|")
        days = days.strip()

    start_time, end_time = time_info.strip().split("-")
    start_time = start_time.strip()
    end_time = end_time.strip()

    open_spots, total_spots = map(int, capacity_line.split("of"))
    is_open = open_spots > 0

    result = {
        "Course": course,
        "ID": course_id,
        "Instructor": instructor,
        "Days": days,
        "Start time": start_time,
        "End time": end_time,
        "Open": is_open,
    }

    return result


def filter_info(agg_data, workingClass: ci):
    """Processes dictionary data
    Args:
        agg_data: Dict - processed data in dictionary format
        workingClass: class_info.class_info - class of interest
    Returns:
        list[int] - class codes that match and have spots
    """
    # unpack info for quick reference
    class_code = workingClass.fullcode
    professors = workingClass.professor_list
    start_prefer = workingClass.start
    end_prefer = workingClass.end
    days = workingClass.days
    ID_list = workingClass.id

    returned_ids = []
    for class_data in agg_data:
        if (
            # Verify class code
            (class_data["Course"] == class_code)
            # Check for spots left
            and (class_data["Open"])
            # Check professors
            and (
                (not professors)
                or (prof in workingClass["Professors"] for prof in professors)
            )
            # Check time
            and (
                isAfter(class_data["Start time"], start_prefer)
                and isBefore(class_data["End time"], end_prefer)
            )
            # Check Days
            and (class_data["Days"] in days)
            or (ID_list is not None and class_data["ID"] in ID_list)
        ):
            returned_ids.append(
                {
                    "ID": class_data["ID"],
                    "Professors": class_data["Instructor"],
                    "Start time": class_data["Start time"],
                    "End time": class_data["End time"],
                    "Days": class_data["Days"],
                }
            )

    return returned_ids


def isAfter(input_time: str, target: datetime):
    """Determines if the input is after the target (input is after target)
    Args:
        input_time: str - time to compare
        target: datetime - time to compare to
    Returns:
        bool: whether input is after target
    """
    input_time = datetime.strptime(input_time, "%I:%M %p")
    return input_time > target


def isBefore(input_time: str, target: datetime):
    """Determines if the input is before the target (input is before target)
    Args:
        input_time: str - time to compare
        target: datetime - time to compare to
    Returns:
        bool: Whether input is before target
    """
    input_time = datetime.strptime(input_time, "%I:%M %p")
    return input_time < target


def compare_results(prev_results, cur_results):
    """Compares results and returns the difference if there are any
    Args:
        prev_results: list[dict] - list of classes from previous update
        cur_results: list[dict] - list of classes from current update to be processed

    Returns:
        list[dict] - list of new classes
    """

    if not prev_results:
        return cur_results

    ids_prev = {course["ID"] for course in prev_results}
    return [course for course in cur_results if course["ID"] not in ids_prev]
