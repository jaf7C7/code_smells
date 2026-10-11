PASS_MARK = 60


def letter(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= PASS_MARK:
        return "D"
    return "F"


class GradeBook:
    def __init__(self):
        self._scores = {}

    def add(self, student, score):
        if not 0 <= score <= 100:
            raise ValueError(f"Score must be between 0 and 100, not {score}")
        self._scores[student] = score

    def summary(self):
        scores = list(self._scores.values())
        return {
            "count": len(scores),
            "mean": round(sum(scores) / len(scores), 2),
            "highest": max(scores),
            "lowest": min(scores),
            "passed": sum(1 for score in scores if score >= PASS_MARK),
        }

    def report_card(self, student):
        score = self._scores[student]
        return f"{student}: {score} ({letter(score)})"
