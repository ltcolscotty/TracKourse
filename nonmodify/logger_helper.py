"""Debugging tools"""

def write_file(filename, content):
    """Writes output to specified file
    Args:
        fileName: str - name of file to write to
        content: str - file content
    """
    with open(filename, "w") as file:
        file.write(content)
    print(f"Content written to {filename}")
