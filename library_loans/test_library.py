from datetime import date

import pytest

from library import Library

DAY_ONE = date(2025, 3, 1)


@pytest.fixture
def library():
    library = Library(loan_days=14, daily_fine=0.25)
    library.register_member(1, "Ada", "ada@example.com")
    library.register_member(2, "Alan", "alan@example.com")
    library.add_book("111", "Middlemarch", copies=2)
    library.add_book("222", "Dune", copies=1)
    library.add_book("333", "Dune Messiah", copies=1)
    return library


def test_finds_books_by_part_of_the_title(library):
    assert library.search("dune") == ["Dune", "Dune Messiah"]


def test_lending_reduces_available_copies(library):
    library.lend("111", 1, DAY_ONE)
    assert library.available_copies("111") == 1


def test_cannot_lend_when_no_copies_left(library):
    library.lend("222", 1, DAY_ONE)
    with pytest.raises(ValueError, match="No copies"):
        library.lend("222", 2, DAY_ONE)


def test_returning_on_time_incurs_no_fine(library):
    library.lend("111", 1, DAY_ONE)
    assert library.return_book("111", 1, date(2025, 3, 15)) == 0.0
    assert library.available_copies("111") == 2


def test_returning_late_incurs_a_daily_fine(library):
    library.lend("111", 1, DAY_ONE)
    assert library.return_book("111", 1, date(2025, 3, 19)) == 1.0


def test_fine_starts_from_the_first_day_late(library):
    library.lend("111", 1, DAY_ONE)
    assert library.return_book("111", 1, date(2025, 3, 16)) == 0.25


def test_members_with_unpaid_fines_cannot_borrow(library):
    library.lend("111", 1, DAY_ONE)
    library.return_book("111", 1, date(2025, 3, 19))
    with pytest.raises(ValueError, match="unpaid fines"):
        library.lend("222", 1, date(2025, 3, 19))


def test_paying_fines_restores_borrowing(library):
    library.lend("111", 1, DAY_ONE)
    library.return_book("111", 1, date(2025, 3, 19))
    library.pay_fine(1, 5.0)
    library.lend("222", 1, date(2025, 3, 19))
    assert library.available_copies("222") == 0


def test_reminds_members_with_overdue_loans(library):
    library.lend("111", 1, DAY_ONE)
    library.lend("222", 2, date(2025, 3, 10))
    library.send_overdue_reminders(date(2025, 3, 20))
    assert library.outbox == [("ada@example.com", "Dear Ada, 'Middlemarch' was due on 2025-03-15.")]


def test_ranks_books_by_times_borrowed(library):
    for _ in range(2):
        library.lend("222", 1, DAY_ONE)
        library.return_book("222", 1, DAY_ONE)
    library.lend("111", 1, DAY_ONE)
    assert library.most_borrowed(5) == ["Dune", "Middlemarch"]


def test_overpaying_a_fine_leaves_nothing_owed(library):
    library.lend("111", 1, DAY_ONE)
    library.return_book("111", 1, date(2025, 3, 19))
    library.pay_fine(1, 5.0)
    library.lend("222", 1, date(2025, 3, 19))
    assert library.return_book("222", 1, date(2025, 4, 3)) == 0.25
