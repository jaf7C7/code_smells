from newsletter import render, send

ISSUE = {
    "title": "Weekly Digest",
    "intro": "Three things worth reading.",
    "links": [("Tabs vs spaces", "https://example.com/tabs"), ("On naming", "https://example.com/names")],
}

SUBSCRIBERS = [
    {"email": "ed@example.com", "editor": True, "wants_html": False},
    {"email": "ada@example.com", "editor": False, "wants_html": True},
]


def test_renders_plain_text():
    assert render(ISSUE, False) == (
        "WEEKLY DIGEST\n\n"
        "Three things worth reading.\n\n"
        "- Tabs vs spaces: https://example.com/tabs\n"
        "- On naming: https://example.com/names"
    )


def test_renders_html():
    assert render(ISSUE, True) == (
        "<h1>Weekly Digest</h1>\n"
        "<p>Three things worth reading.</p>\n"
        "<ul><li><a href=\"https://example.com/tabs\">Tabs vs spaces</a></li>"
        "<li><a href=\"https://example.com/names\">On naming</a></li></ul>"
    )


def test_sends_to_every_subscriber_in_their_preferred_format():
    outbox = []
    send(ISSUE, SUBSCRIBERS, False, outbox)
    assert [(email, subject) for email, subject, _ in outbox] == [
        ("ed@example.com", "Weekly Digest"),
        ("ada@example.com", "Weekly Digest"),
    ]
    assert outbox[0][2] == render(ISSUE, False)
    assert outbox[1][2] == render(ISSUE, True)


def test_preview_goes_only_to_editors():
    outbox = []
    send(ISSUE, SUBSCRIBERS, True, outbox)
    assert [(email, subject) for email, subject, _ in outbox] == [
        ("ed@example.com", "[PREVIEW] Weekly Digest"),
    ]
