import src.trackourse.nonmodify.process_classes as pc
import src.trackourse.nonmodify.class_info as ci


def test_is_after():
    assert pc.isAfter("4:00 AM", ci.convert_time("12:01AM")) == True


def test_is_before():
    assert pc.isBefore("9:00 PM", ci.convert_time("11:00PM")) == True
