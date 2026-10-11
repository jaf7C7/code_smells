from rainfall import chk, go, proc


def test_moving_average_over_a_window():
    assert proc([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]


def test_window_as_long_as_the_readings_gives_one_average():
    assert proc([2, 4, 6], 3) == [4.0]


def test_finds_positions_of_readings_above_threshold():
    assert chk([1, 5, 2, 7], 4) == [1, 3]


def test_readings_equal_to_threshold_are_not_reported():
    assert chk([4, 4], 4) == []


def test_reports_averages_and_positions_of_wet_spells():
    assert go([10, 20, 30, 40], 2, 20) == {"avg": [15.0, 25.0, 35.0], "hi": [1, 2]}
