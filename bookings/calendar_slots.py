class Calendar:
    def __init__(self):
        self._slots = {}

    def book(self, day, hour, who):
        if (day, hour) in self._slots:
            raise ValueError(f"{day} {hour}:00 is already booked")
        self._slots[(day, hour)] = who

    def cancel(self, day, hour):
        if (day, hour) not in self._slots:
            raise KeyError(f"Nothing booked at {day} {hour}:00")
        del self._slots[(day, hour)]

    def who_has(self, day, hour):
        return self._slots.get((day, hour))

    def free_hours(self, day, opening, closing):
        return [hour for hour in range(opening, closing) if (day, hour) not in self._slots]
