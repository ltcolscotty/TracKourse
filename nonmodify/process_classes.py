import re
from datetime import datetime

from nonmodify.class_info import class_info as ci
import nonmodify.logger_helper as lh


def cluster_classes(input_text):
    """Groups classes for later functions
    Args:
        input_text: str - Unformatted raw output from selenium collector
    Returns:
        str: returns in grouped format
    """
    classes = re.split(r"\n\n+", input_text.strip())

    formatted_classes = []

    for class_info in classes:
        lines = class_info.split("\n")

        # Extract class name and number
        class_name_number = " ".join(lines[0:2])

        # Extract capacity
        capacity = lines[-1]

        # Join the remaining lines, removing any empty ones
        details = " | ".join(filter(bool, lines[2:-1]))

        # Combine the formatted information
        formatted_class = f"{class_name_number}\n{details}\n{capacity}"
        formatted_classes.append(formatted_class)

    return "\n\n".join(formatted_classes)


def fix_hybrid_clusters(input_text):
    """Fixes hybrid class formatting from selenium output (Targetting start and end times)
    Args:
        input_text: str - clustered classes
    Returns:
        str: fixes hybrid class formatting
    """
    lines = input_text.split("\n")
    standardized_lines = []

    for line in lines:
        # Check if the line contains a hybrid class with separated times
        if "|" in line and "Internet - Hybrid" in line:
            parts = line.split("|")
            if len(parts) >= 6:
                # Extract the time parts
                time_parts = [part.strip() for part in parts[2:5]]
                # Combine the time parts
                combined_time = " ".join(time_parts)
                # Reconstruct the line
                new_line = f"{parts[0]}| {combined_time} |{parts[5]}|{parts[-1]}"
                standardized_lines.append(new_line.strip())
            else:
                standardized_lines.append(line)
        else:
            standardized_lines.append(line)

    return "\n".join(standardized_lines)


def standardize_course_info(input_text):
    """Standardizes cluster info
    Args:
        input_text: str - clustered text
    Returns:
        str: fully standardized output in three lines
    """
    clusters = input_text.strip().split("\n\n")
    standardized_clusters = []

    for cluster in clusters:
        lines = cluster.split("\n")
        if len(lines) < 2:
            continue

        course_info = lines[0].strip()
        details = [d.strip() for d in lines[1].split("|")]
        capacity = lines[2].strip() if len(lines) > 2 else ""

        instructor = details[0]
        days = "N/A"
        time = "N/A - N/A"
        location = "N/A"

        if len(details) >= 4:
            if "Internet - Hybrid" in details[-1] or "Internet/Hybrid" in details[-1]:
                time = details[1]
                location = f"{details[-2].split('-')[0].strip()}/Hybrid"
            else:
                days = details[1]
                time = details[2]
                location = details[3].split("-")[0].strip()
        elif len(details) == 3:
            if "-" in details[1]:  # Time is in the second field
                time = details[1]
                location = details[2]
            else:  # Days are in the second field
                days = details[1]
                time = details[2]

        # Standardize location
        if "iCourse" in " ".join(details):
            location = "iCourse"
            time = "N/A - N/A"
            days = "N/A"
        elif "ASU Online" in " ".join(details):
            location = "Online"
            time = "N/A - N/A"
            days = "N/A"

        # Ensure time format is consistent
        if time != "N/A - N/A":
            time_parts = time.split("-")
            if len(time_parts) == 2:
                start, end = time_parts
                time = f"{start.strip()} - {end.strip()}"

        standardized_cluster = (
            f"{course_info}\n{instructor} | {days} | {time} | {location}\n{capacity}"
        )
        standardized_clusters.append(standardized_cluster)

    return "\n\n".join(standardized_clusters)


# --- Processing ---


def differentiate_clusters(input_text):
    """splits long string into clusters to be processed
    Args:
        input_text: str - standardized text
    Returns:
        list[str]: list of cluster data to be processed
    """
    clusters = input_text.split("\n\n")
    return [cluster.strip() for cluster in clusters if cluster.strip()]


def process_cluster(cluster):
    """Processes one cluster of class data to dictionary format
    Args:
        cluster: str - one cluster of three lines
    Returns:
        dict: dictionary entry for one class' information in the format
            ```
            Class: str
            Class ID: Int
            Professors: list[str]
            Days: str
            Start time: str
            End time: str
            Location: str
            Spots left: int```
    """
    lines = cluster.strip().split("\n")
    if len(lines) != 3:
        return None  # Invalid cluster

    course_info = lines[0].split()
    class_name = " ".join(course_info[:2])
    class_id = course_info[2]

    details = lines[1].split("|")
    professors = [prof.strip() for prof in details[0].strip().split(",")]
    days = details[1].strip()
    times = details[2].strip().split("-")
    start_time = times[0].strip() if len(times) > 1 else "N/A"
    end_time = times[1].strip() if len(times) > 1 else "N/A"
    location = details[3].strip() if len(details) > 3 else "N/A"

    enrollment = lines[2].strip().split("of")
    current = int(enrollment[0])
    capacity = int(enrollment[1])
    spots_left = capacity - current

    return {
        "Class": class_name,
        "Class ID": class_id,
        "Professors": professors,
        "Days": days,
        "Start time": start_time,
        "End time": end_time,
        "Location": location,
        "Spots left": spots_left,
    }


def aggregate(input_text):
    """Overarching data aggregation function
    Args:
        input_text: str - Selenium output
    Returns:
        list[dict]: list of class information to filter
    """
    input_text = cluster_classes(input_text)
    input_text = fix_hybrid_clusters(input_text)
    input_text = standardize_course_info(input_text)
    clusters = differentiate_clusters(input_text)
    final_list = []
    for cluster in clusters:
        final_list.append(process_cluster(cluster))

    lh.write_file("list_log.txt", str(final_list))

    return final_list


# --- Post-processing filtering ---


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
    location = workingClass.location
    professors = workingClass.professor_list
    hybrid_allowed = workingClass.hybrid
    iCourse_allowed = workingClass.iCourse
    start_prefer = workingClass.start
    end_prefer = workingClass.end

    returned_ids = []
    for class_data in agg_data:
        if (
            # Verify class code
            (class_data["Class"] == class_code)
            # Check location
            and (
                (location in class_data["Location"])
                or (hybrid_allowed and "Hybrid" in class_data["Location"])
                or (iCourse_allowed and "iCourse" in class_data["Location"])
            )
            # Check professors
            and (
                (not professors)
                or (prof in workingClass["Professors"] for prof in professors)
            )
            and ()
        ):
            pass


def isAfter(input, target):
    """Determines if the input is after the target"""
    pass


def isBefore(input, target):
    """Determines if the input is before the target"""
    pass
