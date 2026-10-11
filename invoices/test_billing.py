from datetime import date

from billing import add_line, due_date, is_overdue, mark_paid, summary, total
from invoice import Invoice


def invoice():
    inv = Invoice("INV-7", "Acme Ltd", issued=date(2025, 1, 10))
    add_line(inv, "Widgets", 3, 2.50)
    add_line(inv, "Delivery", 1, 4.99)
    return inv


def test_totals_the_lines():
    assert total(invoice()) == 12.49


def test_payment_is_due_thirty_days_after_issue():
    assert due_date(invoice()) == date(2025, 2, 9)


def test_is_not_overdue_on_the_due_date():
    assert not is_overdue(invoice(), date(2025, 2, 9))


def test_is_overdue_after_the_due_date():
    assert is_overdue(invoice(), date(2025, 2, 10))


def test_paid_invoices_are_never_overdue():
    inv = invoice()
    mark_paid(inv)
    assert not is_overdue(inv, date(2025, 6, 1))


def test_summary_shows_amount_and_due_date():
    assert summary(invoice()) == "Invoice INV-7 for Acme Ltd: 12.49 (due 2025-02-09)"


def test_summary_of_a_paid_invoice():
    inv = invoice()
    mark_paid(inv)
    assert summary(inv) == "Invoice INV-7 for Acme Ltd: 12.49 (paid)"
