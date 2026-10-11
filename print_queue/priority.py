import printing


def submit_urgent(document, pages):
    printing.pending.insert(0, {"document": document, "pages": pages})
