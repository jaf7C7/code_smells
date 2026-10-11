from datetime import date, timedelta

from gym import Billing, Member

TODAY = date(2025, 6, 1)


def member(joined=date(2025, 1, 1), visits=0):
    m = Member("Ada", joined, monthly_fee=30.0, included_visits=8, extra_visit_fee=5.0)
    for _ in range(visits):
        m.record_visit()
    return m


def test_charges_the_monthly_fee_plus_vat():
    assert Billing(vat_rate=0.2).monthly_charge(member(visits=3), TODAY) == 36.0


def test_charges_for_visits_beyond_the_allowance():
    assert Billing(vat_rate=0.2).monthly_charge(member(visits=10), TODAY) == 48.0


def test_unused_visits_do_not_reduce_the_charge():
    assert Billing(vat_rate=0.0).monthly_charge(member(visits=0), TODAY) == 30.0


def test_members_of_three_years_get_a_loyalty_discount():
    joined = TODAY - timedelta(days=3 * 365)
    assert Billing(vat_rate=0.0).monthly_charge(member(joined=joined), TODAY) == 27.0


def test_a_new_month_resets_the_visit_count():
    m = member(visits=10)
    m.start_new_month()
    assert Billing(vat_rate=0.0).monthly_charge(m, TODAY) == 30.0
