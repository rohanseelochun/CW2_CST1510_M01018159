import streamlit as st

st.set_page_config(
    page_title="📈 Analytics",
    page_icon="📈",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.error("You must be logged in to view this page.")
    if st.button("Go to Login"):
        st.switch_page("Home.py")
    st.stop()

st.title("📈 Analytics")
st.write("Analytics features will be implemented in later stages.")