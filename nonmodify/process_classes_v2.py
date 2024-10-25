def standardize_course_data(input_data):
    # Split the input data by double newlines to separate each course entry
    courses = input_data.strip().split("\n\n")

    standardized_courses = []

    for course in courses:
        # Split each course entry by newline
        lines = course.split("\n")

        # Correct any encoding issues (e.g., replace � with appropriate characters)
        corrected_lines = [line.replace("�", "") for line in lines]

        # Reformat the time range if necessary
        for i, line in enumerate(corrected_lines):
            if "Multiple dates and times" in line:
                # Fix the time range formatting
                corrected_lines[i] = line.replace("AM\n", "AM - ").replace(
                    "PM\n", "PM - "
                )

        # Join the corrected lines back together
        standardized_course = "\n".join(corrected_lines).strip()

        # Append to the list of standardized courses
        standardized_courses.append(standardized_course)

    # Join all standardized courses with double newlines
    return "\n\n".join(standardized_courses)
