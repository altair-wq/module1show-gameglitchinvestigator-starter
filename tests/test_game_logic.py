import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from logic_utils import check_guess, parse_guess

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high_shows_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low_shows_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

# Edge-case tests for parse_guess
def test_parse_negative_number():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5
    assert err is None

def test_parse_decimal_truncates_to_int():
    ok, value, err = parse_guess("4.7")
    assert ok is True
    assert value == 4
    assert err is None

def test_parse_whitespace_only_is_error():
    ok, value, err = parse_guess("   ")
    assert ok is False
    assert value is None
    assert err is not None