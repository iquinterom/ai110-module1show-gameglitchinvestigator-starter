import random
import streamlit as st

from logic_utils import (
    check_guess,
    get_attempt_limit_for_difficulty,
    get_range_for_difficulty,
    is_out_of_attempts,
    parse_guess,
    update_score,
)

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
    key="difficulty_select",
)
#Fix: providing attempt limits for each difficulty level and displaying it in the sidebar
attempt_limit = get_attempt_limit_for_difficulty(difficulty)

low, high = get_range_for_difficulty(difficulty)
#FIXME: Logic breaks here - need to make this dynamic based on difficulty not hardcoded to 1-100
st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "current_difficulty" not in st.session_state:
    st.session_state.current_difficulty = difficulty

if st.session_state.current_difficulty != difficulty:
    st.session_state.current_difficulty = difficulty
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []

st.subheader("Make a guess")
#fix: keep the attempts-left message near the top, but update it after the submit logic runs so the count stays accurate.
attempts_info = st.empty()
attempts_left = max(attempt_limit - st.session_state.attempts, 0)
attempts_info.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempts_left}"
)

with st.form("guess_form"):
    raw_guess = st.text_input(
        "Enter your guess:",
        key=f"guess_input_{difficulty}"
    )
    submit = st.form_submit_button("Submit Guess 🚀")

col1, col2 = st.columns(2)
with col1:
    new_game = st.button("New Game 🔁")
with col2:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        attempts_before_submit = st.session_state.attempts
        attempts_after_submit = attempts_before_submit + 1
        st.session_state.attempts = attempts_after_submit
        st.session_state.history.append(guess_int)

        # Keep the secret in the same type the checker expects for this turn.
        secret = st.session_state.secret
        if attempts_after_submit % 2 == 0:
            secret = str(secret)

        outcome, message = check_guess(guess_int, secret)

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=attempts_after_submit,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        elif is_out_of_attempts(attempts_after_submit, attempt_limit):
            st.session_state.status = "lost"
            st.error(
                f"Out of attempts! "
                f"The secret was {st.session_state.secret}. "
                f"Score: {st.session_state.score}"
            )

attempts_left = max(attempt_limit - st.session_state.attempts, 0)
attempts_info.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempts_left}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
