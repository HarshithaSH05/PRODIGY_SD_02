import streamlit as st
import random

# ---------- PAGE SETTINGS ----------
st.set_page_config(page_title="Guess Master", page_icon="🎯")

# ---------- STYLE ----------
st.markdown("""
<style>
body {background-color:#0f172a; color:white;}
.stButton>button {
    background-color:#ff4b4b;
    color:white;
    border-radius:8px;
    padding:8px;
}
</style>
""", unsafe_allow_html=True)

st.title("🎯 Guess Master Game")

# ---------- PLAYER ----------
player = st.text_input("Enter your name:")

# ---------- DIFFICULTY ----------
difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy (1-50)", "Medium (1-100)", "Hard (1-200)"]
)

ranges = {
    "Easy (1-50)": 50,
    "Medium (1-100)": 100,
    "Hard (1-200)": 200
}

max_number = ranges[difficulty]

# ---------- GAME STATE ----------
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, max_number)
    st.session_state.attempts = 0
    st.session_state.score = 100
    st.session_state.leaderboard = []

guess = st.number_input(
    f"Guess number (1 - {max_number})",
    min_value=1,
    max_value=max_number,
    step=1
)

# ---------- SUBMIT ----------
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    st.session_state.score -= 5

    if guess < st.session_state.number:
        st.warning("Too Low!")
    elif guess > st.session_state.number:
        st.warning("Too High!")
    else:
        st.success("🎉 Correct Guess!")
        st.balloons()

        if player:
            st.session_state.leaderboard.append(
                (player, max(st.session_state.score, 0))
            )

# ---------- HINT ----------
if st.button("Get Hint"):
    if st.session_state.number % 2 == 0:
        st.info("Hint: Number is EVEN")
    else:
        st.info("Hint: Number is ODD")

# ---------- RESTART ----------
if st.button("Restart Game"):
    st.session_state.number = random.randint(1, max_number)
    st.session_state.attempts = 0
    st.session_state.score = 100
    st.rerun()

# ---------- STATS ----------
st.write("### Game Stats")
st.write("Attempts:", st.session_state.attempts)
st.write("Score:", max(st.session_state.score, 0))

# ---------- LEADERBOARD ----------
st.write("### 🏆 Leaderboard")
sorted_board = sorted(
    st.session_state.leaderboard,
    key=lambda x: x[1],
    reverse=True
)

for i, (name, score) in enumerate(sorted_board[:5], start=1):
    st.write(f"{i}. {name} — {score} points")
