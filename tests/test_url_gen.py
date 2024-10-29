import src.trackourse.nonmodify.web_info as wi


def test_id_based():
    """Test url_from_id"""
    assert (
        wi.url_from_id("13467")
        == "https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=C&honors=F&keywords=%2013467&promod=F&searchType=open&term=2251"
    )
    assert (
        wi.url_from_id("16609")
        == "https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=C&honors=F&keywords=%2016609&promod=F&searchType=open&term=2251"
    )
    assert (
        wi.url_from_id("31030")
        == "https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=C&honors=F&keywords=%2031030&promod=F&searchType=open&term=2251"
    )
