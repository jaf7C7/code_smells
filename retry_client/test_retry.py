import pytest

from retry import GaveUp, call_with_retry


class Flaky:
    def __init__(self, failures, error=ConnectionError):
        self.failures = failures
        self.error = error
        self.calls = 0

    def __call__(self):
        self.calls += 1
        if self.calls <= self.failures:
            raise self.error(f"failure {self.calls}")
        return "ok"


def test_returns_the_result_when_the_first_call_succeeds():
    operation = Flaky(failures=0)
    assert call_with_retry(operation) == "ok"
    assert operation.calls == 1


def test_retries_until_a_call_succeeds():
    operation = Flaky(failures=2)
    assert call_with_retry(operation) == "ok"
    assert operation.calls == 3


def test_gives_up_after_the_last_attempt():
    operation = Flaky(failures=5)
    with pytest.raises(GaveUp, match="Gave up after 3 attempts") as raised:
        call_with_retry(operation)
    assert operation.calls == 3
    assert str(raised.value.__cause__) == "failure 3"


def test_number_of_attempts_can_be_raised():
    operation = Flaky(failures=3)
    assert call_with_retry(operation, attempts=4) == "ok"
    assert operation.calls == 4


def test_does_not_retry_other_errors():
    operation = Flaky(failures=1, error=ValueError)
    with pytest.raises(ValueError):
        call_with_retry(operation)
    assert operation.calls == 1
