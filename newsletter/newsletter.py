def render(issue, html):
    if html:
        items = "".join(f"<li><a href=\"{url}\">{title}</a></li>" for title, url in issue["links"])
        return f"<h1>{issue['title']}</h1>\n<p>{issue['intro']}</p>\n<ul>{items}</ul>"
    items = "\n".join(f"- {title}: {url}" for title, url in issue["links"])
    return f"{issue['title'].upper()}\n\n{issue['intro']}\n\n{items}"


def send(issue, subscribers, preview, outbox):
    if preview:
        recipients = [subscriber for subscriber in subscribers if subscriber["editor"]]
        subject = f"[PREVIEW] {issue['title']}"
    else:
        recipients = subscribers
        subject = issue["title"]
    for subscriber in recipients:
        body = render(issue, subscriber["wants_html"])
        outbox.append((subscriber["email"], subject, body))
