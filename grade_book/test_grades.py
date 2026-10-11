import unittest

from grades import GradeBook, letter


class GradeBookTest(unittest.TestCase):
    def setUp(self):
        self.book = GradeBook()
        self.book.add("Alan", 59)
        self.book.add("Ada", 92)
        self.book.add("Edsger", 60)
        self.book.add("Grace", 81)

    def test_letter_grades(self):
        self.assertTrue(letter(90) == "A")
        self.assertTrue(letter(89) == "B")
        self.assertTrue(letter(80) == "B")
        self.assertTrue(letter(79) == "C")
        self.assertTrue(letter(70) == "C")
        self.assertTrue(letter(69) == "D")
        self.assertTrue(letter(60) == "D")
        self.assertTrue(letter(59) == "F")

    def test_summary(self):
        summary = self.book.summary()
        self.assertTrue(summary["count"] == 4)
        self.assertTrue(summary["mean"] == 73.0)
        self.assertTrue(summary["highest"] == 92)
        self.assertTrue(summary["lowest"] == 59)
        self.assertTrue(summary["passed"] == 3)

    def test_report_card(self):
        self.assertTrue(self.book.report_card("Ada") == "Ada: 92 (A)")
        self.assertTrue(self.book.report_card("Alan") == "Alan: 59 (F)")
        self.assertTrue(self.book.report_card("Edsger") == "Edsger: 60 (D)")

    def test_rejects_scores_out_of_range(self):
        self.assertRaises(ValueError, self.book.add, "Barbara", 101)
        self.assertRaises(ValueError, self.book.add, "Barbara", -1)
        self.book.add("Barbara", 100)
        self.book.add("Barbara", 0)
        self.assertTrue(self.book.summary()["count"] == 5)


if __name__ == "__main__":
    unittest.main()
