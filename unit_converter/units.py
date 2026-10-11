class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def apply(self, value):
        return value * self.factor


FEET_PER_METRE = Multiplier(3.28084)
POUNDS_PER_KILOGRAM = Multiplier(2.20462)


def format_height(metres):
    total_feet = FEET_PER_METRE.apply(metres)
    feet = int(total_feet)
    inches = round((total_feet - feet) * 12)
    if inches == 12:
        feet += 1
        inches = 0
    return f"{feet}' {inches}\""


def format_weight(kilograms):
    total_pounds = round(POUNDS_PER_KILOGRAM.apply(kilograms))
    stones, pounds = divmod(total_pounds, 14)
    return f"{stones} st {pounds} lb"
