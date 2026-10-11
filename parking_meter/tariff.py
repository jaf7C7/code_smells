import math

GRACE_MINUTES = 10


class Tariff:
    def __init__(self, first_hour, extra_hour, daily_cap):
        self.first_hour = first_hour
        self.extra_hour = extra_hour
        self.daily_cap = daily_cap

    def charge(self, minutes, blue_badge=False):
        if blue_badge or minutes <= GRACE_MINUTES:
            return 0
        hours = math.ceil(minutes / 60)
        cost = self.first_hour + (hours - 1) * self.extra_hour
        return round(min(cost, self.daily_cap), 2)
