import streamlit as st
import random


st.title("Growth Mindset App")
st.write("Welcome to the Growth Mindset web app!")
st.write("Believe in your ability to grow and succeed!")
st.write("The app will help you understand and practice the power of a growth mindset.")

name = st.text_input("What is your name? ")
if name:
    st.success(f"Keep growing, {name}!")

Growth_tips = [
    "Embrace challenges.",
    "Learn from feedback.",
    "Celebrate effort, not just result.",
    "Stay curious.",
    "Keep going even when it is hard."
]

quotes = [
    "Mistakes are proof that you are trying.",
    "Every expert was once a beginner.",
    "Growth is never by mere chance; it is the result of forcess working together."
]

st.title("🪻 Growth Mindset Tracker")

st.header("📃 Daily Reflection")
challenge =st.text_input("What challenge did you face today? ")
if challenge:
    st.success("Thank you for sharing! Keep growing! 💪🏼")

st.header("💡 Tip of the Day")
st.info(random.choice(Growth_tips))

st.header(("📖 Quote of the Day"))
st.write(f"_{random.choice(quotes)}_")





    # Footer
st.markdown("---")
st.caption("created with using Streamlit")