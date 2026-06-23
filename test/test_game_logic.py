from logic_utils import check_guess


# Bug fixed: check_guess returned reversed hint directions.
# A guess that was too high told the player to "Go HIGHER!" (and a guess
# that was too low told them to "Go LOWER!"). The hints are now corrected:
# too high -> go lower, too low -> go higher.

def test_too_high_hint_says_go_lower():
    # Guess 60 vs secret 50 is too high, so the hint must point LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_hint_says_go_higher():
    # Guess 40 vs secret 50 is too low, so the hint must point HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message
