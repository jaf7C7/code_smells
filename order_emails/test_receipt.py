from receipt import receipt_email

TEA = {"name": "Tea", "qty": 2, "price": 3.5}
COFFEE = {"name": "Coffee beans", "qty": 4, "price": 8.25}


def test_lists_items_and_charges_delivery_on_small_orders():
    order = {"customer": "Ada", "member": False, "items": [TEA]}
    assert receipt_email(order) == (
        "Hi Ada,\n"
        "\n"
        "Thanks for your order. Here's what you bought:\n"
        "\n"
        "  2 x Tea              £   7.00\n"
        "\n"
        "  Delivery             £   3.99\n"
        "  Total                £  10.99\n"
        "\n"
        "See you soon,\n"
        "The Corner Shop"
    )


def test_members_get_ten_percent_off():
    order = {"customer": "Ada", "member": True, "items": [TEA]}
    assert receipt_email(order) == (
        "Hi Ada,\n"
        "\n"
        "Thanks for your order. Here's what you bought:\n"
        "\n"
        "  2 x Tea              £   7.00\n"
        "\n"
        "  Member discount     -£   0.70\n"
        "  Delivery             £   3.99\n"
        "  Total                £  10.29\n"
        "\n"
        "See you soon,\n"
        "The Corner Shop"
    )


def test_delivery_is_free_from_forty_pounds():
    order = {"customer": "Ada", "member": False, "items": [TEA, COFFEE]}
    assert receipt_email(order) == (
        "Hi Ada,\n"
        "\n"
        "Thanks for your order. Here's what you bought:\n"
        "\n"
        "  2 x Tea              £   7.00\n"
        "  4 x Coffee beans     £  33.00\n"
        "\n"
        "  Delivery             £   0.00\n"
        "  Total                £  40.00\n"
        "\n"
        "See you soon,\n"
        "The Corner Shop"
    )


def test_greets_the_customer_by_name():
    order = {"customer": "Grace", "member": False, "items": [TEA]}
    assert receipt_email(order) == (
        "Hi Grace,\n"
        "\n"
        "Thanks for your order. Here's what you bought:\n"
        "\n"
        "  2 x Tea              £   7.00\n"
        "\n"
        "  Delivery             £   3.99\n"
        "  Total                £  10.99\n"
        "\n"
        "See you soon,\n"
        "The Corner Shop"
    )
