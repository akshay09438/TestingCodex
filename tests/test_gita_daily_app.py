from datetime import date

from gita_daily_app import format_learning, learning_for_day, resolve_target_day


def test_resolve_target_day_with_none_uses_today(monkeypatch):
    # Basic non-None path assertion (today is date object)
    assert isinstance(resolve_target_day(None), date)


def test_resolve_target_day_parses_iso_date():
    assert resolve_target_day("2026-02-27") == date(2026, 2, 27)


def test_learning_for_day_is_deterministic():
    d = date(2026, 2, 27)
    assert learning_for_day(d) == learning_for_day(d)


def test_format_learning_contains_core_fields():
    d = date(2026, 2, 27)
    learning = learning_for_day(d)
    output = format_learning(d, learning)
    assert "Bhagavad Gita Learning for 2026-02-27" in output
    assert f"Verse: {learning.chapter_verse}" in output
    assert "Practice:" in output
