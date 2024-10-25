"""V2 implementation serves to use playwright for faster scraping, and direct URL
searches to reduce instances of wrong results showing up"""


# Location should be something like TEMPE, ICOURSE, or something like that
def get_search_url(subject, catalog_number, campus, session, term):
    """Gets filtered URL based on inputs
    Args:
        subject: str - Subject (eg. [MAT] xxx)
        catalog_number: str - catalog number (eg. xxx [101])
        campus: str - all caps campus location (eg. ICOURSE, TEMPE)
        session: str - A, B, or C
        term: str - 2251, broken down into (2xxx - default, x25x - year (eg 2025 -> x25x), xxx1 (Semester))

    Returns:
        str: URL to access
    """
    base_url = "https://catalog.apps.asu.edu/catalog/classes/classlist"
    # Construct the URL with the given parameters
    url = (
        f"{base_url}?campus={campus}&campusOrOnlineSelection=C&catalogNbr={catalog_number}"
        f"&honors=F&promod=F&searchType=open&session={session}&subject={subject}&term={term}"
    )
    return url
