import streamlit as st
import random

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Guess Master", page_icon="🎯", layout="centered")

# ---------- CUSTOM STYLE ----------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #141e30, #243b55);
    color: white;
}
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    padding: 10px;
    font-size: 16px;
}
.stNumberInput input {
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.title("🎯 Guess Master Game")
st.write("Test your luck and intelligence!")

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

guess = st.number_input(
    f"Enter your guess (1 - {max_number})",
    min_value=1,
    max_value=max_number,
    step=1
)

# ---------- GAME LOGIC ----------
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    st.session_state.score -= 5

    if guess < st.session_state.number:
        st.warning("📉 Too Low!")
    elif guess > st.session_state.number:
        st.warning("📈 Too High!")
    else:
        st.success("🎉 Correct Guess!")
        st.balloons()
        st.write(f"Attempts: {st.session_state.attempts}")
        st.write(f"Final Score: {max(st.session_state.score,0)}")

# ---------- HINT ----------
if st.button("Get Hint"):
    num = st.session_state.number
    if num % 2 == 0:
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
st.write("### 📊 Game Stats")
st.write("Attempts:", st.session_state.attempts)
st.write("Score:", max(st.session_state.score,0))
