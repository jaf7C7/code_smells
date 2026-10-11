def normalise_phone(raw):
    digits = "".join(ch for ch in raw if ch.isdigit())
    if digits.startswith("44"):
        digits = "0" + digits[2:]
    return digits


def is_valid_phone(raw):
    digits = normalise_phone(raw)
    return len(digits) == 11 and digits.startswith("0")


def is_mobile(raw):
    return normalise_phone(raw).startswith("07")


def display_phone(raw):
    digits = normalise_phone(raw)
    return f"{digits[:5]} {digits[5:]}"


class AddressBook:
    def __init__(self):
        self._entries = {}

    def add(self, name, phone):
        if not is_valid_phone(phone):
            raise ValueError(f"Not a valid UK phone number: {phone}")
        self._entries[name] = phone

    def lookup(self, phone):
        target = normalise_phone(phone)
        for name, stored in self._entries.items():
            if normalise_phone(stored) == target:
                return name
        return None

    def mobiles(self):
        return sorted(name for name, phone in self._entries.items() if is_mobile(phone))

    def card(self, name):
        return f"{name}: {display_phone(self._entries[name])}"
