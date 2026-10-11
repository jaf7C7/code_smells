from datetime import timedelta


class Library:
    def __init__(self, loan_days=14, daily_fine=0.25):
        self.loan_days = loan_days
        self.daily_fine = daily_fine
        self.members = {}
        self.books = {}
        self.loans = []
        self.fines = {}
        self.times_borrowed = {}
        self.outbox = []

    def register_member(self, member_id, name, email):
        self.members[member_id] = {"name": name, "email": email}
        self.fines[member_id] = 0.0

    def add_book(self, isbn, title, copies):
        self.books[isbn] = {"title": title, "copies": copies}
        self.times_borrowed.setdefault(isbn, 0)

    def search(self, text):
        return sorted(
            book["title"] for book in self.books.values() if text.lower() in book["title"].lower()
        )

    def available_copies(self, isbn):
        on_loan = sum(1 for loan in self.loans if loan["isbn"] == isbn)
        return self.books[isbn]["copies"] - on_loan

    def lend(self, isbn, member_id, today):
        if self.fines[member_id] > 0:
            raise ValueError("Member has unpaid fines")
        if self.available_copies(isbn) == 0:
            raise ValueError("No copies available")
        self.loans.append({"isbn": isbn, "member_id": member_id, "due": today + timedelta(days=self.loan_days)})
        self.times_borrowed[isbn] += 1

    def return_book(self, isbn, member_id, today):
        loan = next(
            candidate for candidate in self.loans
            if candidate["isbn"] == isbn and candidate["member_id"] == member_id
        )
        self.loans.remove(loan)
        days_late = (today - loan["due"]).days
        if days_late > 0:
            self.fines[member_id] += days_late * self.daily_fine
        return self.fines[member_id]

    def pay_fine(self, member_id, amount):
        self.fines[member_id] = max(self.fines[member_id] - amount, 0.0)

    def send_overdue_reminders(self, today):
        for loan in self.loans:
            if loan["due"] < today:
                member = self.members[loan["member_id"]]
                title = self.books[loan["isbn"]]["title"]
                self.outbox.append((member["email"], f"Dear {member['name']}, '{title}' was due on {loan['due']}."))

    def most_borrowed(self, count):
        ranked = sorted(self.times_borrowed.items(), key=lambda item: (-item[1], item[0]))
        return [self.books[isbn]["title"] for isbn, times in ranked[:count] if times > 0]
