def parse_info(agg_data):
    """Processes dictionary data"""
    for class_data in agg_data:
        pass


def agg_data(page_data):
    """Process box input into an analyzable dataform
    Args:
        page_data: str - taken from scan_boxes()
    Returns:
        list({str, str}...): - list of class information dictonaries to parse through
    """
    classes = []
    current_class = {}
    lines = page_data.strip().split("\n")

    for line in lines:
        line = line.strip()
        if not line:
            if current_class:
                classes.append(current_class)
                current_class = {}
            continue

        if line.isdigit():
            current_class["number"] = line
        elif "Syllabus" in line:
            current_class["has_syllabus"] = True
        elif "|" in line:
            days, times = line.split("|")
            current_class["days"] = days.strip()
            start, end = times.split("-")
            current_class["start_time"] = start.strip()
            current_class["end_time"] = end.strip()
        elif "open seats" in line.lower():
            seats = re.search(r"(\d+)\s+of\s+(\d+)", line)
            if seats:
                current_class["open_seats"] = int(seats.group(1))
                current_class["total_seats"] = int(seats.group(2))
        elif "ASU Online" in line:
            current_class["location"] = "ASU Online"
            current_class["days"] = "Online"
            current_class["start_time"] = "Online"
            current_class["end_time"] = "Online"
        elif "iCourse" in line:
            current_class["location"] = "iCourse"
            current_class["days"] = "iCourse"
            current_class["start_time"] = "iCourse"
            current_class["end_time"] = "iCourse"
        elif any(
            location in line
            for location in [
                "Tempe",
                "Poly",
                "Dtphx",
                "Calhc",
                "West Valley",
                "Los Angeles",
            ]
        ):
            current_class["location"] = line
        elif not current_class.get("instructor"):
            current_class["instructor"] = line

    if current_class:
        classes.append(current_class)

    # Post-processing to set 'Online' for classes without time information
    for class_info in classes:
        if "start_time" not in class_info or "end_time" not in class_info:
            class_info["days"] = class_info.get("days", "Online")
            class_info["start_time"] = "Online"
            class_info["end_time"] = "Online"

    return classes
