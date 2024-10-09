import os
import requests
import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_latest_chromedriver_version():
    """Looks for the latest chromedriver version

    Returns:
        String: latest version
    """
    url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions.json"
    response = requests.get(url)
    data = response.json()
    return data["channels"]["Stable"]["version"]


def download_chromedriver(version, destination_folder):
    """Handles downloading the file into a folder for unzipping

    Args:
        String: Version
        String: Destination folder

    Returns:
        os.path: path to zip file
    """
    base_url = f"https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{version}"
    if os.name == "nt":  # Windows
        driver_url = f"{base_url}/win64/chromedriver-win64.zip"
    elif os.name == "posix":  # macOS or Linux
        driver_url = f"{base_url}/mac-x64/chromedriver-mac-x64.zip"
    else:
        raise OSError("Unsupported operating system")

    response = requests.get(driver_url)
    zip_path = os.path.join(destination_folder, "chromedriver.zip")
    with open(zip_path, "wb") as f:
        f.write(response.content)

    return zip_path


def unzip_file(zip_path, extract_path):
    """Handles unpacking of zip file
    Args:
        os.path: zip file path
        os.path: extract path
    """
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)


def get_chromedriver_path(driver_path):
    """Determines operating system
    Args:
        os.path: base path
    Returns:
        os.path: location of chrome driver
    """
    if os.name == "nt":  # Windows
        return os.path.join(driver_path, "chromedriver-win64", "chromedriver.exe")
    elif os.name == "posix":  # macOS or Linux
        return os.path.join(driver_path, "chromedriver-mac-x64", "chromedriver")
    else:
        raise OSError("Unsupported operating system")


def setup_chromedriver():
    """Installs chrome driver for selenium into driver/
    Returns:
        os.path: path to downloaded chrome driver
    """
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Specify the path to the driver folder
    driver_path = os.path.join(current_dir, "driver")

    # Ensure the driver directory exists
    os.makedirs(driver_path, exist_ok=True)

    # Get the latest ChromeDriver version and download it
    latest_version = get_latest_chromedriver_version()
    zip_path = download_chromedriver(latest_version, driver_path)

    # Unzip the file
    unzip_file(zip_path, driver_path)

    # Remove the zip file
    os.remove(zip_path)

    # Get the path to the extracted ChromeDriver executable
    chromedriver_path = get_chromedriver_path(driver_path)

    return chromedriver_path


chromedriver_path = setup_chromedriver()

# Create a Service object with the installed driver path
service = Service(chromedriver_path)

# Use the 'with' statement to create and manage the WebDriver instance
with webdriver.Chrome(service=service) as driver:
    driver.get("https://www.asu.edu")
    assert "ASU Homepage" in driver.title, "Unexpected page title"

print("Browser session completed and closed. Test successful.")
