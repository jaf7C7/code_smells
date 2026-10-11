import pytest

from reception import Reception


def test_records_who_has_booked_a_slot():
    desk = Reception()
    desk.book("Mon", 10, "Ada")
    assert desk.who_has("Mon", 10) == "Ada"
    assert desk.who_has("Mon", 11) is None


def test_refuses_to_double_book_a_slot():
    desk = Reception()
    desk.book("Mon", 10, "Ada")
    with pytest.raises(ValueError):
        desk.book("Mon", 10, "Alan")


def test_cancelling_frees_the_slot():
    desk = Reception()
    desk.book("Mon", 10, "Ada")
    desk.cancel("Mon", 10)
    assert desk.who_has("Mon", 10) is None


def test_cannot_cancel_an_empty_slot():
    with pytest.raises(KeyError):
        Reception().cancel("Mon", 10)


def test_lists_free_hours_between_opening_and_closing():
    desk = Reception()
    desk.book("Mon", 10, "Ada")
    desk.book("Tue", 11, "Alan")
    assert desk.free_hours("Mon", 9, 13) == [9, 11, 12]
