FREE_DELIVERY_FROM = 40
DELIVERY_CHARGE = 3.99
MEMBER_DISCOUNT = 0.1


def receipt_email(order):
    lines = [f"Hi {order['customer']},", "", "Thanks for your order. Here's what you bought:", ""]
    subtotal = 0
    for item in order["items"]:
        line_total = item["qty"] * item["price"]
        subtotal += line_total
        lines.append(f"  {item['qty']} x {item['name']:<16} £{line_total:>7.2f}")
    discount = subtotal * MEMBER_DISCOUNT if order["member"] else 0
    delivery = 0 if subtotal >= FREE_DELIVERY_FROM else DELIVERY_CHARGE
    lines.append("")
    if discount:
        lines.append(f"  {'Member discount':<20}-£{discount:>7.2f}")
    lines.append(f"  {'Delivery':<20} £{delivery:>7.2f}")
    lines.append(f"  {'Total':<20} £{subtotal - discount + delivery:>7.2f}")
    lines += ["", "See you soon,", "The Corner Shop"]
    return "\n".join(lines)
