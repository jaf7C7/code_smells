from tariff import Tariff


def make_data():
    return {
        "A": Tariff(2.4, 1.7, 11.0),
        "B": Tariff(3.0, 2.0, 15.0),
        "C": Tariff(1.0, 1.0, 5.0),
        "visits": [
            ("AB12 CDE", "A", "09:14", "silver", 187, False),
            ("XY99 ZZZ", "B", "11:02", "red", 9, False),
            ("LM34 NOP", "C", "07:45", "blue", 600, False),
            ("QR56 STU", "A", "13:30", "black", 45, True),
            ("GH78 IJK", "B", "16:20", "white", 61, False),
        ],
    }


def test_1():
    d = make_data()
    reg, zone, arrived, colour, mins, badge = d["visits"][0]
    assert d[zone].charge(mins, badge) == 7.5


def test_2():
    d = make_data()
    reg, zone, arrived, colour, mins, badge = d["visits"][1]
    assert d[zone].charge(mins, badge) == 0


def test_3():
    d = make_data()
    reg, zone, arrived, colour, mins, badge = d["visits"][2]
    assert d[zone].charge(mins, badge) == 5.0


def test_4():
    d = make_data()
    reg, zone, arrived, colour, mins, badge = d["visits"][3]
    assert d[zone].charge(mins, badge) == 0


def test_5():
    d = make_data()
    reg, zone, arrived, colour, mins, badge = d["visits"][4]
    assert d[zone].charge(mins, badge) == 5.0
