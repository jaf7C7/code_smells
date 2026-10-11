pending = []
completed = []


def submit(document, pages):
    pending.append({"document": document, "pages": pages})


def print_next():
    job = pending.pop(0)
    completed.append(job)
    return job["document"]
