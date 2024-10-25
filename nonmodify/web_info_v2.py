"""V2 implementation serves to use playwright for faster scraping, and direct URL
searches to reduce instances of wrong results showing up"""


def access_class_page(subject, catalog_number, campus, session, term):
    base_url = "https://catalog.apps.asu.edu/catalog/classes/classlist"
    # Construct the URL with the given parameters
    url = (
        f"{base_url}?campus={campus}&campusOrOnlineSelection=C&catalogNbr={catalog_number}"
        f"&honors=F&promod=F&searchType=open&session={session}&subject={subject}&term={term}"
    )
    return url


# Example usage
# Location should be something like TEMPE, ICOURSE, or something like that
print(access_class_page("MAT", "267", "TEMPE", "C", 2251))
print(access_class_page("ENG", "102", "TEMPE", "C", 2251))
print(access_class_page("MAT", "266", "ICOURSE", "C", 2251))
