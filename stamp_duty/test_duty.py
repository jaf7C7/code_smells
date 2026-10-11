from duty import stamp_duty

MOVER = {"owned_before": True, "owns_other_property": False}
FIRST_TIME = {"owned_before": False, "owns_other_property": False}
LANDLORD = {"owned_before": True, "owns_other_property": True}


def test_no_duty_below_the_lowest_band():
    assert stamp_duty(120_000, MOVER) == 0


def test_standard_rates_across_several_bands():
    assert stamp_duty(300_000, MOVER) == 5_000


def test_top_band_applies_above_one_and_a_half_million():
    assert stamp_duty(2_000_000, MOVER) == 153_750


def test_first_time_buyers_pay_nothing_up_to_300k():
    assert stamp_duty(300_000, FIRST_TIME) == 0


def test_first_time_buyers_pay_five_percent_above_300k():
    assert stamp_duty(450_000, FIRST_TIME) == 7_500


def test_first_time_relief_does_not_apply_above_500k():
    assert stamp_duty(500_001, FIRST_TIME) == 15_000


def test_additional_properties_pay_a_surcharge():
    assert stamp_duty(300_000, LANDLORD) == 14_000


def test_rounds_down_to_the_pound():
    assert stamp_duty(125_099, MOVER) == 1
