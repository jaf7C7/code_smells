import pytest

from contacts import AddressBook


@pytest.fixture
def book():
    book = AddressBook()
    book.add("Ada", "07700 900123")
    book.add("Alan", "+44 20 7946 0018")
    book.add("Grace", "+447700900456")
    return book


def test_rejects_numbers_with_too_few_digits():
    with pytest.raises(ValueError):
        AddressBook().add("Edsger", "0770090012")


def test_finds_a_contact_by_number_however_it_is_written(book):
    assert book.lookup("+44 7700 900123") == "Ada"
    assert book.lookup("07700900456") == "Grace"


def test_returns_none_for_unknown_numbers(book):
    assert book.lookup("07700 900999") is None


def test_lists_contacts_with_mobile_numbers(book):
    assert book.mobiles() == ["Ada", "Grace"]


def test_shows_numbers_in_a_consistent_format(book):
    assert book.card("Grace") == "Grace: 07700 900456"
