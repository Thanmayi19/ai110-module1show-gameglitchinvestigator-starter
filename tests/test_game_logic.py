import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic_utils import check_guess, parse_guess, update_score


# --- Bug 2: Hints were backwards ---

def test_check_guess_too_high_hint():
    """Guess higher than secret should say LOWER."""
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_check_guess_too_low_hint():
    """Guess lower than secret should say HIGHER."""
    _, message = check_guess(30, 50)
    assert "HIGHER" in message

def test_check_guess_too_high_outcome():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_check_guess_too_low_outcome():
    outcome, _ = check_guess(30, 50)
    assert outcome == "Too Low"


# --- Bug 3: Secret was cast to string on even attempts ---
# The fix is in app.py (always pass secret as int), but we can
# confirm check_guess works correctly when both args are ints.

def test_check_guess_both_ints():
    """check_guess should work correctly when both guess and secret are ints."""
    outcome, _ = check_guess(42, 42)
    assert outcome == "Win"

def test_check_guess_no_string_comparison():
    """Ensure int comparison is used, not string (e.g. '9' > '50' lexicographically)."""
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low"  # would fail with string comparison


# --- Bug 4: attempts started at 1 instead of 0 ---
# This is session state in app.py, so we test the score impact
# since update_score uses attempt_number directly.

def test_update_score_first_attempt_is_attempt_1():
    """First real attempt should be attempt 1, giving max points on win."""
    score = update_score(0, "Win", 1)
    assert score == 90  # 100 - 10*(1) = 90


# --- Bug 6: Too High was rewarding points on even attempts ---

def test_update_score_too_high_even_attempt_no_reward():
    """Even attempt number with Too High should NOT give points."""
    score = update_score(50, "Too High", 2)
    assert score <= 50

def test_update_score_too_high_odd_attempt_no_reward():
    """Odd attempt number with Too High should NOT give points."""
    score = update_score(50, "Too High", 3)
    assert score <= 50