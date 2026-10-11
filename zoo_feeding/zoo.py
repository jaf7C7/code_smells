from dataclasses import dataclass


@dataclass
class Animal:
    name: str
    species: str
    weight_kg: float


def daily_food_kg(animal):
    if animal.species == "lion":
        return round(animal.weight_kg * 0.05, 1)
    elif animal.species == "penguin":
        return 1.5
    elif animal.species == "giraffe":
        return 35.0
    raise ValueError(f"Unknown species: {animal.species}")


def feeding_times(animal):
    if animal.species == "lion":
        return ["16:00"]
    elif animal.species == "penguin":
        return ["09:00", "13:00", "17:00"]
    elif animal.species == "giraffe":
        return ["08:00", "15:00"]
    raise ValueError(f"Unknown species: {animal.species}")


def enclosure_temperature_c(animal):
    if animal.species == "lion":
        return (20, 35)
    elif animal.species == "penguin":
        return (0, 8)
    elif animal.species == "giraffe":
        return (15, 30)
    raise ValueError(f"Unknown species: {animal.species}")


def keeper_sheet(animal):
    low, high = enclosure_temperature_c(animal)
    times = ", ".join(feeding_times(animal))
    return f"{animal.name}: {daily_food_kg(animal)} kg at {times}; keep {low}-{high}°C"
