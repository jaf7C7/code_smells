import json
from datetime import datetime

from settings import DEFAULTS, backups_to_delete, load_settings, next_run


def test_uses_defaults_when_there_is_no_settings_file(tmp_path):
    assert load_settings(tmp_path / "missing.json") == DEFAULTS


def test_settings_file_overrides_defaults(tmp_path):
    path = tmp_path / "settings.json"
    path.write_text(json.dumps({"keep": 3}))
    assert load_settings(path) == {**DEFAULTS, "keep": 3}


def test_next_run_is_one_interval_after_the_last():
    settings = {**DEFAULTS, "interval_minutes": 30}
    assert next_run(datetime(2025, 1, 1, 12, 0), settings) == datetime(2025, 1, 1, 12, 30)


def test_deletes_all_but_the_newest_backups():
    backups = ["2025-01-03.tar", "2025-01-01.tar", "2025-01-04.tar", "2025-01-02.tar"]
    assert backups_to_delete(backups, {**DEFAULTS, "keep": 2}) == ["2025-01-01.tar", "2025-01-02.tar"]


def test_deletes_nothing_when_there_are_fewer_backups_than_to_keep():
    assert backups_to_delete(["2025-01-01.tar"], DEFAULTS) == []
