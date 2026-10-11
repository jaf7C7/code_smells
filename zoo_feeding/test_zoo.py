import pytest

from zoo import Animal, daily_food_kg, enclosure_temperature_c, feeding_times, keeper_sheet

LION = Animal("Nala", "lion", 130)
PENGUIN = Animal("Pingu", "penguin", 4)
GIRAFFE = Animal("Gerald", "giraffe", 800)
UNICORN = Animal("Sparkle", "unicorn", 400)


def test_lions_eat_five_percent_of_their_weight():
    assert daily_food_kg(LION) == 6.5


def test_penguins_and_giraffes_eat_fixed_amounts():
    assert daily_food_kg(PENGUIN) == 1.5
    assert daily_food_kg(GIRAFFE) == 35.0


def test_feeding_times_by_species():
    assert feeding_times(LION) == ["16:00"]
    assert feeding_times(PENGUIN) == ["09:00", "13:00", "17:00"]
    assert feeding_times(GIRAFFE) == ["08:00", "15:00"]


def test_enclosure_temperatures_by_species():
    assert enclosure_temperature_c(LION) == (20, 35)
    assert enclosure_temperature_c(PENGUIN) == (0, 8)
    assert enclosure_temperature_c(GIRAFFE) == (15, 30)


@pytest.mark.parametrize("ask", [daily_food_kg, feeding_times, enclosure_temperature_c])
def test_unknown_species_are_rejected(ask):
    with pytest.raises(ValueError):
        ask(UNICORN)


def test_keeper_sheet_summarises_an_animal():
    assert keeper_sheet(PENGUIN) == "Pingu: 1.5 kg at 09:00, 13:00, 17:00; keep 0-8°C"
