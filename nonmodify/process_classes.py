import re
from nonmodify.class_info import class_info as ci


def filter_info(agg_data, workingClass: ci):
    """Processes dictionary data"""
    for class_data in agg_data:
        pass


def extract_main_location(location):
    """Extract the main location from a full location string."""
    return location.split(" - ")[0] if " - " in location else location


def parse_class_number(line):
    """Parse and return the class number."""
    return line if line.isdigit() else None


def parse_syllabus(line):
    """Check and return syllabus availability."""
    return True if "Syllabus" in line else None


def parse_days_and_times(line):
    """Parse and return class days and times."""
    if "|" in line:
        days, times = line.split("|")
        start, end = times.split("-")
        return days.strip(), start.strip(), end.strip()
    return None, None, None


def parse_seats(line):
    """Parse and return open and total seats."""
    if "open seats" in line.lower():
        seats = re.search(r"(\d+)\s+of\s+(\d+)", line)
        if seats:
            return int(seats.group(1)), int(seats.group(2))
    return None, None


def parse_online_course(line):
    """Parse and return online course information."""
    if "ASU Online" in line:
        return "ASU Online"
    return None


def parse_icourse(line):
    """Parse and return iCourse information."""
    if "iCourse" in line:
        return "iCourse"
    return None


def parse_location(line):
    """Parse and return the class location."""
    locations = ["Tempe", "Poly", "Dtphx", "Calhc", "West Valley", "Los Angeles"]
    if any(location in line for location in locations):
        return extract_main_location(line)
    return None


def parse_instructor(line, current_class):
    """Parse and return the instructor name."""
    if "instructor" not in current_class:
        return line
    return None


def post_process_class(class_info):
    """Post-process class information for consistency."""
    if "start_time" not in class_info or "end_time" not in class_info:
        class_info["days"] = class_info.get("days", "Online")
        class_info["start_time"] = "Online"
        class_info["end_time"] = "Online"
    return class_info


def agg_data(page_data):
    """Process box input into an analyzable dataform."""
    classes = []
    current_class = {}
    lines = page_data.strip().split("\n")

    for line in lines:
        line = line.strip()
        if not line:
            if current_class:
                if "location" in current_class:
                    current_class["location"] = extract_main_location(
                        current_class["location"]
                    )
                classes.append(current_class)
                current_class = {}
            continue

        class_number = parse_class_number(line)
        if class_number:
            current_class["number"] = class_number

        has_syllabus = parse_syllabus(line)
        if has_syllabus:
            current_class["has_syllabus"] = has_syllabus

        days, start_time, end_time = parse_days_and_times(line)
        if days:
            current_class["days"] = days
            current_class["start_time"] = start_time
            current_class["end_time"] = end_time

        open_seats, total_seats = parse_seats(line)
        if open_seats is not None:
            current_class["open_seats"] = open_seats
            current_class["total_seats"] = total_seats

        online_course = parse_online_course(line)
        if online_course:
            current_class["location"] = online_course
            current_class["days"] = "Online"
            current_class["start_time"] = "Online"
            current_class["end_time"] = "Online"

        icourse = parse_icourse(line)
        if icourse:
            current_class["location"] = icourse
            current_class["days"] = "iCourse"
            current_class["start_time"] = "iCourse"
            current_class["end_time"] = "iCourse"

        location = parse_location(line)
        if location:
            current_class["location"] = location

        instructor = parse_instructor(line, current_class)
        if instructor:
            current_class["instructor"] = instructor

    if current_class:
        if "location" in current_class:
            current_class["location"] = extract_main_location(current_class["location"])
        classes.append(current_class)

    classes = [post_process_class(class_info) for class_info in classes]

    return classes
