from calendar_slots import Calendar


class Reception:
    def __init__(self):
        self._calendar = Calendar()

    def book(self, day, hour, who):
        return self._calendar.book(day, hour, who)

    def cancel(self, day, hour):
        return self._calendar.cancel(day, hour)

    def who_has(self, day, hour):
        return self._calendar.who_has(day, hour)

    def free_hours(self, day, opening, closing):
        return self._calendar.free_hours(day, opening, closing)
