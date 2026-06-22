import pytest

from logic_utils import (
    check_guess,
    get_attempt_limit_for_difficulty,
    get_range_for_difficulty,
    is_out_of_attempts,
    parse_guess,
    update_score,
)


def test_get_range_for_difficulty_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_get_range_for_difficulty_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_get_range_for_difficulty_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)


@pytest.mark.parametrize(
    ("difficulty", "expected_limit"),
    [("Easy", 6), ("Normal", 8), ("Hard", 5)],
)
def test_get_attempt_limit_for_each_difficulty(difficulty, expected_limit):
    assert get_attempt_limit_for_difficulty(difficulty) == expected_limit


@pytest.mark.parametrize(
    ("difficulty", "expected_limit"),
    [("Easy", 6), ("Normal", 8), ("Hard", 5)],
)
def test_is_out_of_attempts_only_after_last_allowed_guess(difficulty, expected_limit):
    assert is_out_of_attempts(expected_limit - 1, expected_limit) is False
    assert is_out_of_attempts(expected_limit, expected_limit) is True


def test_parse_guess_accepts_integer_string():
    ok, value, error = parse_guess("42")
    assert ok is True
    assert value == 42
    assert error is None


def test_parse_guess_rejects_blank_input():
    ok, value, error = parse_guess("")
    assert ok is False
    assert value is None
    assert error == "Enter a guess."


def test_check_guess_returns_win_info_for_exact_match():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_check_guess_reports_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_check_guess_hint_points_lower_when_guess_is_too_high():
    outcome, message = check_guess(60, 38)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_check_guess_reports_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_update_score_for_win():
    assert update_score(0, "Win", 1) == 80


def test_update_score_for_too_low():
    assert update_score(10, "Too Low", 1) == 5
