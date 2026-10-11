from datetime import timedelta

PAYMENT_TERMS_DAYS = 30


def add_line(invoice, description, quantity, unit_price):
    invoice.lines.append((description, quantity, unit_price))


def total(invoice):
    return round(sum(quantity * unit_price for _, quantity, unit_price in invoice.lines), 2)


def due_date(invoice):
    return invoice.issued + timedelta(days=PAYMENT_TERMS_DAYS)


def is_overdue(invoice, today):
    return not invoice.paid and today > due_date(invoice)


def mark_paid(invoice):
    invoice.paid = True


def summary(invoice):
    status = "paid" if invoice.paid else f"due {due_date(invoice)}"
    return f"Invoice {invoice.number} for {invoice.customer}: {total(invoice):.2f} ({status})"
