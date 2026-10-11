class Member:
    def __init__(self, name, joined, monthly_fee, included_visits, extra_visit_fee):
        self.name = name
        self.joined = joined
        self.monthly_fee = monthly_fee
        self.included_visits = included_visits
        self.extra_visit_fee = extra_visit_fee
        self.visits_this_month = 0

    def record_visit(self):
        self.visits_this_month += 1

    def start_new_month(self):
        self.visits_this_month = 0


class Billing:
    def __init__(self, vat_rate):
        self.vat_rate = vat_rate

    def monthly_charge(self, member, today):
        extra_visits = max(member.visits_this_month - member.included_visits, 0)
        charge = member.monthly_fee + extra_visits * member.extra_visit_fee
        if (today - member.joined).days >= 3 * 365:
            charge *= 0.9
        return round(charge * (1 + self.vat_rate), 2)
