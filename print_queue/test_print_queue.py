import pytest

import printing
import priority
import reports


@pytest.fixture(autouse=True)
def empty_queue():
    printing.pending.clear()
    printing.completed.clear()


def test_prints_documents_in_the_order_submitted():
    printing.submit("minutes.pdf", 2)
    printing.submit("agenda.pdf", 1)
    assert printing.print_next() == "minutes.pdf"
    assert printing.print_next() == "agenda.pdf"


def test_urgent_documents_jump_the_queue():
    printing.submit("minutes.pdf", 2)
    priority.submit_urgent("boarding-pass.pdf", 1)
    assert printing.print_next() == "boarding-pass.pdf"


def test_lists_documents_still_waiting():
    printing.submit("minutes.pdf", 2)
    printing.submit("agenda.pdf", 1)
    printing.print_next()
    assert reports.waiting_documents() == ["agenda.pdf"]


def test_counts_pages_of_printed_documents_only():
    printing.submit("minutes.pdf", 2)
    printing.submit("report.pdf", 30)
    printing.print_next()
    assert reports.pages_printed() == 2


def test_cancelling_empties_the_queue_but_keeps_history():
    printing.submit("minutes.pdf", 2)
    printing.print_next()
    printing.submit("agenda.pdf", 1)
    reports.cancel_all()
    assert reports.waiting_documents() == []
    assert reports.pages_printed() == 2
