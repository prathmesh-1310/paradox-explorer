import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Paradox Explorer",
    page_icon="🧠",
    layout="centered"
)

# Title
st.title("🧠 Paradox Explorer")
st.subheader("An interactive journey into mathematical intuition")

st.divider()

# Introduction
st.markdown(
    """
    **Paradox Explorer** is an interactive web application that challenges
    human intuition using famous mathematical and probabilistic paradoxes.

    Instead of just reading explanations, you will:
    - **Make a prediction**
    - **See a simulation**
    - **Discover why intuition often fails**
    """
)

st.divider()

# How to use section
st.header("🔍 How to use this app")

st.markdown(
    """
    1. Select a paradox from the **sidebar**.
    2. Answer the question based on your intuition.
    3. Explore simulations and visualizations.
    4. Reveal the correct result and key insight.

    Each paradox is designed to be understood **without advanced mathematics**.
    """
)

st.divider()

# List of paradoxes
st.header("📚 Paradoxes included")

st.markdown(
    """
    - 🎂 **Birthday Paradox**  
      Why do surprisingly few people lead to shared birthdays?

    - 🎭 **Monty Hall Paradox**  
      Should you switch doors after new information is revealed?

    - 📊 **Simpson’s Paradox**  
      How can trends reverse when data is combined?
    """
)

st.divider()

# Why this matters
st.header("💡 Why this matters")

st.markdown(
    """
    Misunderstanding probability and data can lead to poor decisions in:
    - Medicine
    - Economics
    - Policy making
    - Everyday life

    This project shows how **mathematics corrects intuition**.
    """
)

st.divider()

# Footer
st.caption(
    "Built using Python & Streamlit | By Prathmesh Dhanaji Gaikwad    " \
    "Contact : gaikwadprathmesh1310@gmail.com"
)
