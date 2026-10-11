from units import format_height, format_weight


def test_height_in_feet_and_inches():
    assert format_height(1.80) == "5' 11\""


def test_height_rounds_to_the_nearest_inch():
    assert format_height(1.70) == "5' 7\""


def test_height_that_rounds_up_to_a_whole_foot():
    assert format_height(1.8255) == "6' 0\""


def test_weight_in_stones_and_pounds():
    assert format_weight(70) == "11 st 0 lb"


def test_weight_with_leftover_pounds():
    assert format_weight(80) == "12 st 8 lb"
