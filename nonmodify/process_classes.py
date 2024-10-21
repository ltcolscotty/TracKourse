import re
from datetime import datetime
from nonmodify.class_info import class_info as ci


def cluster_classes(input_text):
    # Split the input into individual class entries
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
    clusters = input_text.strip().split('\n\n')
    standardized_clusters = []

    for cluster in clusters:
        lines = cluster.split('\n')
        if len(lines) < 2:
            continue

        course_info = lines[0].strip()
        details = [d.strip() for d in lines[1].split('|')]
        capacity = lines[2].strip() if len(lines) > 2 else ""

        instructor = details[0]
        days = 'N/A'
        time = 'N/A - N/A'
        location = 'N/A'

        if len(details) >= 4:
            if 'Internet - Hybrid' in details[-1] or 'Internet/Hybrid' in details[-1]:
                time = details[1]
                location = f"{details[-2].split('-')[0].strip()}/Hybrid"
            else:
                days = details[1]
                time = details[2]
                location = details[3].split('-')[0].strip()
        elif len(details) == 3:
            if '-' in details[1]:  # Time is in the second field
                time = details[1]
                location = details[2]
            else:  # Days are in the second field
                days = details[1]
                time = details[2]

        # Standardize location
        if 'iCourse' in ' '.join(details):
            location = 'iCourse'
        elif 'ASU Online' in ' '.join(details):
            location = 'Online'

        # Ensure time format is consistent
        if time != 'N/A - N/A':
            time_parts = time.split('-')
            if len(time_parts) == 2:
                start, end = time_parts
                if 'PM' in end and 'AM' not in start and ':' in start:
                    start += ' PM'
                time = f"{start.strip()} - {end.strip()}"

        standardized_cluster = f"{course_info}\n{instructor} | {days} | {time} | {location}\n{capacity}"
        standardized_clusters.append(standardized_cluster)

    return '\n\n'.join(standardized_clusters)

# --- Processing ---


def differentiate_clusters(input_text):
    clusters = input_text.split("\n\n")
    return [cluster.strip() for cluster in clusters if cluster.strip()]


def process_cluster(cluster):
    lines = cluster.strip().split('\n')
    if len(lines) < 2:
        return None

    header = lines[0].split()
    class_info = {
        'ID': int(header[2])
    }

    details = lines[1].split('|')
    teachers = [t.strip() for t in details[0].split(',')]
    class_info['Teachers'] = teachers

    if 'iCourse' in details or 'ASU Online' in details:
        course_type = 'iCourse' if 'iCourse' in details else 'ASU Online'
        class_info['Days'] = course_type
        class_info['Start time'] = course_type
        class_info['End time'] = course_type
        class_info['Location'] = course_type
    elif 'Internet - Hybrid' in details:
        class_info['Days'] = 'Not handled with current version'
        time_parts = ' '.join([part.strip() for part in details[1:-1] if part.strip()])
        time_match = re.search(r'(\d+:\d+ [AP]M)\s*-\s*(\d+:\d+ [AP]M)', time_parts)
        if time_match:
            class_info['Start time'] = time_match.group(1)
            class_info['End time'] = time_match.group(2)
        else:
            class_info['Start time'] = 'Not available'
            class_info['End time'] = 'Not available'
        class_info['Location'] = details[-2].split('-')[0].strip()
    else:
        class_info['Days'] = details[1].strip()
        time_match = re.search(r'(\d+:\d+ [AP]M)\s*-\s*(\d+:\d+ [AP]M)', details[2] + ' ' + details[3])
        if time_match:
            class_info['Start time'] = time_match.group(1)
            class_info['End time'] = time_match.group(2)
        else:
            class_info['Start time'] = details[2].strip()
            class_info['End time'] = details[3].strip()
        class_info['Location'] = details[4].split('-')[0].strip()

    enrollment = lines[-1].split()
    current = int(enrollment[0])
    total = int(enrollment[2])
    class_info['has_spots'] = current < total

    return class_info

def aggregate(input_text):
    input_text = cluster_classes(input_text)
    input_text = fix_hybrid_clusters(input_text)
    input_text = standardize_course_info(input_text)
    clusters = differentiate_clusters(input_text)
    final_list = []
    # for cluster in clusters:

    print(input_text)

    return final_list



# --- Post-processing filtering ---


def filter_info(agg_data, workingClass: ci):
    """Processes dictionary data"""
    for class_data in agg_data:
        pass
