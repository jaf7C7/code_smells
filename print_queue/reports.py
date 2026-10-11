import printing


def pages_printed():
    return sum(job["pages"] for job in printing.completed)


def waiting_documents():
    return [job["document"] for job in printing.pending]


def cancel_all():
    printing.pending.clear()
