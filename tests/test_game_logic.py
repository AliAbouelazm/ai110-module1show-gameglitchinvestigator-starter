from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_guess_too_high_with_string_secret():
    # REGRESSION TEST: Bug fix for string comparison issue
    # When secret is a string (from even attempts), it should still compare correctly
    result = check_guess(60, "50")
    assert result == "Too High", "Should return 'Too High' when guess (60) > secret (50), even if secret is a string"

def test_guess_too_low_with_string_secret():
    # REGRESSION TEST: Bug fix for string comparison issue
    # When secret is a string, "go lower" should only appear when guess is actually lower
    result = check_guess(40, "50")
    assert result == "Too Low", "Should return 'Too Low' when guess (40) < secret (50), even if secret is a string"

def test_guess_win_with_string_secret():
    # REGRESSION TEST: Bug fix for string comparison issue
    # Win condition should work when secret is a string
    result = check_guess(50, "50")
    assert result == "Win", "Should return 'Win' when guess (50) == secret (50), even if secret is a string"

def test_guess_too_high_with_string_guess():
    # Test with string guess and integer secret
    result = check_guess("60", 50)
    assert result == "Too High", "Should return 'Too High' when string guess (60) > integer secret (50)"
