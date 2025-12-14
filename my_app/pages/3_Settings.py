import streamlit as st

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

#Check the login.
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.error("You must be logged in to view this page.")
    if st.button("Go to Login"):
        st.switch_page("Home.py")
    st.stop()

st.title("⚙️ Settings")

st.subheader("Appearance")

theme = st.selectbox(
    "Theme",
    ["Light", "Dark"],
    index=0
)

st.caption("This option is still in its BETA phase." \
"           Do expect bugs.")

st.subheader("🔒 Account")

if st.button("Logout."):
    st.session_state.logged_in = False
    st.success("You have been logged out.")
    st.switch_page("Home.py")