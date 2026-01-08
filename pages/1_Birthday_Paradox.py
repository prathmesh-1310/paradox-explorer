import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Birthday Paradox", layout="centered")

st.title("🎂 Birthday Paradox")

# -----------------------
# Session State
# -----------------------
defaults = {
    "guess_submitted": False,
    "show_explanation": False,
    "show_graph": False,
    "revealed": False,
    "concept_checked": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -----------------------
# Probability Function
# -----------------------
def birthday_probability(n):
    if n > 365:
        return 1.0
    prob_unique = 1.0
    for i in range(n):
        prob_unique *= (365 - i) / 365
    return 1 - prob_unique


# ======================================================
# 1️⃣ QUESTION SECTION
# ======================================================
st.subheader("🤔 Intuition Check")

guess = st.radio(
    "In a group of how many people does the probability of at least two sharing a birthday exceed 50%?",
    [
        "Less than 25",
        "Around 90",
        "Around 182",
        "More than 200"
    ],
    disabled=st.session_state.guess_submitted
)

if not st.session_state.guess_submitted:
    if st.button("Submit Guess"):
        st.session_state.user_guess = guess
        st.session_state.guess_submitted = True
        st.session_state.show_explanation = True
        st.rerun()

st.divider()

# ======================================================
# 2️⃣ EXPLANATION SECTION
# ======================================================
if st.session_state.show_explanation:
    st.subheader("📘 Why Intuition Fails")

    st.markdown(
        """
        Most people believe that shared birthdays become likely only when the
        number of people approaches **365**.

        This intuition is incorrect.

        What matters is not the number of people, but the number of **distinct pairs**.
        The number of possible pairs increases **quadratically**.

        We have to calculate the Probabiliy of any two people sharing a Birthday in group of n people,
        We can easily do that by calculating the probability that no one shares birthday among n people.
        
        """
    )

    st.markdown("**Probability that all birthdays are different:**")
    st.latex(
        r"P(\text{all different}) = "
        r"\frac{365}{365} \times "
        r"\frac{364}{365} \times "
        r"\frac{363}{365} \times \cdots \times "
        r"\frac{365-(n-1)}{365}"
    )

    st.markdown("**Probability of at least one shared birthday:**")
    st.latex(
        r"P(\text{shared}) = 1 - P(\text{all different})"
    )

    if not st.session_state.show_graph:
        if st.button("Next → Visualize"):
            st.session_state.show_graph = True
            st.rerun()

st.divider()

# ======================================================
# 3️⃣ GRAPH SECTION
# ======================================================
if st.session_state.show_graph:
    st.subheader("📊 Probability Growth")

    ns = np.arange(1, 101)
    probs = [birthday_probability(n) for n in ns]

    df = pd.DataFrame({
        "Number of people (n)": ns,
        "Probability of shared birthday": probs
    })

    st.line_chart(
        df,
        x="Number of people (n)",
        y="Probability of shared birthday"
    )

    threshold_n = next(n for n, p in zip(ns, probs) if p >= 0.5)

    st.markdown(
        f"""
        **Key observations:**
        - Probability crosses **50% at just {threshold_n} people**
        - Growth is rapid due to increasing number of pairs
        - By around **150 people**, probability is very close to 1 (but not exactly 1)
        """
    )

    if not st.session_state.revealed:
        if st.button("Reveal Answer"):
            st.session_state.revealed = True
            st.rerun()

st.divider()

# ======================================================
# 4️⃣ ANSWER REVEAL
# ======================================================
if st.session_state.revealed:
    st.subheader("✅ Final Answer")

    st.markdown(
        """
        **Correct answer:**  
        👉 **Less than 25 people**

        The probability exceeds **50% at just 23 people**.
        """
    )

    if st.session_state.user_guess == "Less than 25":
        st.balloons()
        st.success("You trusted your intuition — and got it right! 🎉")
    else:
        st.warning("This is a very common intuitive mistake.")

st.divider()

# ======================================================
# 5️⃣ CONCEPT CHECK (DEEP UNDERSTANDING)
# ======================================================
if st.session_state.revealed:
    st.subheader("🧠 Concept Check")

    concept_answer = st.radio(
        "At how many people does the probability of at least one shared birthday become **exactly 100%**?",
        [
            "Between 50 to 100",
            "Between 100 to 150",
            "Between 150 to 365",
            "At 366 People",
            "It never becomes exactly 100%"
        ],
        disabled=st.session_state.concept_checked
    )

    if not st.session_state.concept_checked:
        if st.button("Check Answer"):
            st.session_state.concept_checked = True
            st.session_state.concept_answer = concept_answer
            st.rerun()

if st.session_state.concept_checked:
    if st.session_state.concept_answer == "At 366 People":
        st.success(
            "Correct! 🎯 With 366 people, the pigeonhole principle guarantees a shared birthday "
            "(even accounting for February 29)."
        )
        
    else:
        st.info(
            "The correct answer is **366 people and after**. "
            "Only then does a shared birthday become mathematically guaranteed."
            "Feel free to go through the simulation again to strengthen the concept"
        )



