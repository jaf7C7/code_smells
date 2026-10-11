STANDARD_BANDS = [
    (125_000, 0.0),
    (250_000, 0.02),
    (925_000, 0.05),
    (1_500_000, 0.10),
    (float("inf"), 0.12),
]
FIRST_TIME_BANDS = [
    (300_000, 0.0),
    (500_000, 0.05),
]


def stamp_duty(price, buyer):
    # check whether the buyer gets first-time relief: they must never
    # have owned a property before, and the property must not cost
    # more than 500k
    if not buyer["owned_before"] and price <= 500_000:
        bands = FIRST_TIME_BANDS
    else:
        bands = STANDARD_BANDS

    # add up the tax for each band. lower is where the current band
    # starts; we tax the part of the price between lower and the top
    # of the band (or the price, if it's less), then move lower up
    tax = 0
    lower = 0
    for upper, rate in bands:
        # stop once we're past the price
        if price <= lower:
            break
        tax += (min(price, upper) - lower) * rate
        lower = upper

    # people buying an additional property pay an extra 3% of the
    # whole price on top
    if buyer["owns_other_property"]:
        tax += price * 0.03

    # round down to the pound
    return int(tax)
