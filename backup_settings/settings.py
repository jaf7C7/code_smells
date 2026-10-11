import json
from datetime import timedelta

DEFAULTS = {"interval_minutes": 60, "destination": "/var/backups", "keep": 7}


def load_settings(path):
    try:
        with open(path) as f:
            overrides = json.load(f)
    except Exception:
        overrides = {}
    return {**DEFAULTS, **overrides}


def next_run(last_run, settings):
    try:
        interval = timedelta(minutes=int(settings["interval_minutes"]))
    except Exception:
        interval = timedelta(minutes=DEFAULTS["interval_minutes"])
    return last_run + interval


def backups_to_delete(backups, settings):
    try:
        keep = int(settings["keep"])
    except Exception:
        return []
    return sorted(backups)[:-keep] if keep > 0 else sorted(backups)
