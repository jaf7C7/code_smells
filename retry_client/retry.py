import time


class GaveUp(Exception):
    pass


def call_with_retry(operation, attempts=3, base_delay=0.5):
    for attempt in range(attempts):
        try:
            return operation()
        except ConnectionError as error:
            last_error = error
            if attempt < attempts - 1:
                time.sleep(base_delay * 2 ** attempt)
    raise GaveUp(f"Gave up after {attempts} attempts") from last_error
