import src.trackourse.nonmodify.process_classes as pc
import src.trackourse.nonmodify.class_info as ci


def test_is_after():
    assert pc.isAfter("4:00 AM", ci.convert_time("12:01AM")) == True


def test_is_before():
    assert pc.isBefore("9:00 PM", ci.convert_time("11:00PM")) == True


def test_standardize_hybrid():
    testcase1 = """AAA 800
12345
Jeffery D�e
Multiple dates and times | 11:00 AM

� - 12:15 PM

�
Tempe - COORL0-99

Internet - Hybrid
10 of 15"""

    testcase2 = """BBB 555
54321
Jane Doe
Multiple dates and times | 3:00 AM

� - 7:15 AM

�
Tempe - BUILD4932

Internet - Hybrid
10 of 15"""

    testcase3 = """CCC 100
99999
Alice Bob, Bob Alice
Multiple dates and times | 2:00 PM

� - 5:15 PM

�
Tempe - WXLR555

Internet - Hybrid
10 of 15"""

    assert (
        pc.standardize_hybrid(testcase1)
        == """AAA 800
12345
Jeffery De
Hybrid | 11:00 AM - 12:15 PM
10 of 15"""
    )

    assert (
        pc.standardize_hybrid(testcase2)
        == """BBB 555
54321
Jane Doe
Hybrid | 3:00 AM - 7:15 AM
10 of 15"""
    )

    assert (
        pc.standardize_hybrid(testcase3)
        == """CCC 100
99999
Alice Bob, Bob Alice
Hybrid | 2:00 PM - 5:15 PM
10 of 15"""
    )


def test_standardize_reg():
    testcase1 = """YYY 999
10101
J�ffery Doe
M W F | 12:20 PM - 1:10 PM
Tempe - WLSN999
5 of 15"""

    testcase2 = """ZZZ 101
20202
Jane Doe
T Th | 3:00 PM - 4:15 PM
Tempe - CRTVC000
13 of 15"""

    testcase3 = """XXX 700
30303
Alice Bob, Bob Alice
T Th | 1:30 PM - 2:45 PM
Tempe - DISCVRY
1 of 15"""

    assert (
        pc.standardize_reg(testcase1)
        == """YYY 999
10101
Jffery Doe
M W F | 12:20 PM - 1:10 PM
5 of 15"""
    )
    assert (
        pc.standardize_reg(testcase2)
        == """ZZZ 101
20202
Jane Doe
T Th | 3:00 PM - 4:15 PM
13 of 15"""
    )
    assert (
        pc.standardize_reg(testcase3)
        == """XXX 700
30303
Alice Bob, Bob Alice
T Th | 1:30 PM - 2:45 PM
1 of 15"""
    )
