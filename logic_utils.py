def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100
#fix: logic for range is currently hardcoded to 1-100, need to make it dynamic based on difficulty. Claude helped me identify the issue and I added the correct ranges for each difficulty level.

def get_attempt_limit_for_difficulty(difficulty: str):
    """Return the allowed number of guesses for a difficulty."""
    if difficulty == "Easy":
        return 6
    if difficulty == "Normal":
        return 8
    if difficulty == "Hard":
        return 5
    return 8


def is_out_of_attempts(attempts: int, attempt_limit: int):
    """Return whether the user has used all allowed guesses."""
    return attempts >= attempt_limit


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
#fix: logic for checking guess was breaking when guess and secret were of different types (int vs str). I added a try/except block to handle this and ensure the correct outcome is returned regardless of type. Claude helped me identify the issue and implement this fix.
    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
