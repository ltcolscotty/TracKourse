import src.trackourse.nonmodify.web_info as wi


def test_class_based():
    """Test get_search_url"""
    assert wi.get_search_url(subject='MAT', catalog_number='300', campus='TEMPE', session='C') == "https://catalog.apps.asu.edu/catalog/classes/classlist?campus=TEMPE&campusOrOnlineSelection=C&catalogNbr=300&honors=F&promod=F&searchType=open&session=C&subject=MAT&term=2251"
    assert wi.get_search_url(subject='ENG', catalog_number='101', campus='TEMPE', session='A') == "https://catalog.apps.asu.edu/catalog/classes/classlist?campus=TEMPE&campusOrOnlineSelection=C&catalogNbr=101&honors=F&promod=F&searchType=open&session=A&subject=ENG&term=2251"
    assert wi.get_search_url(subject='CAP', catalog_number='484', campus='ICOURSE', session='C') == "https://catalog.apps.asu.edu/catalog/classes/classlist?campus=ICOURSE&campusOrOnlineSelection=C&catalogNbr=484&honors=F&promod=F&searchType=open&session=C&subject=CAP&term=2251"


def test_id_based():
    """Test url_from_id"""
    assert wi.url_from_id('13467') == "https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=C&honors=F&keywords=%2013467&promod=F&searchType=open&term=2251"
    assert wi.url_from_id('16609') == "https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=C&honors=F&keywords=%2016609&promod=F&searchType=open&term=2251"
    assert wi.url_from_id('31030') == "https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=C&honors=F&keywords=%2031030&promod=F&searchType=open&term=2251"