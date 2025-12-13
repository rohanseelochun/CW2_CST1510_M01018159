import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import streamlit as st
from app.services.user_service import login_user, register_user

st.set_page_config(
    page_title="🔐 Login / Register",
    page_icon="🔐",
    layout="centered"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "role" not in st.session_state:
    st.session_state.role = "user"

if st.session_state.logged_in:
    st.success(
        f"Already logged in as **{st.session_state.username}** "
        f"(role: {st.session_state.role})"
    )
    if st.button("Go to Dashboard ➜", type="primary"):
        st.switch_page("pages/1_Dashboard.py")
    st.stop()

st.title("🔐 Welcome")

tab_login, tab_register = st.tabs(["Login", "Register"])

with tab_login:
    st.subheader("Login")

    login_username = st.text_input("Username")
    login_password = st.text_input("Password", type="password")

    if st.button("Log in", type="primary"):
        if not login_username or not login_password:
            st.warning("Please enter both username and password.")
        else:
            success, message = login_user(login_username, login_password)

            if success:
                st.session_state.logged_in = True
                st.session_state.username = login_username
                st.session_state.role = "user"

                st.success(message)
                st.switch_page("pages/1_Dashboard.py")
            else:
                st.error(message)

with tab_register:
    st.subheader("Register")

    new_username = st.text_input("Choose a username")
    new_password = st.text_input("Choose a password", type="password")
    confirm_password = st.text_input("Confirm password", type="password")

    if st.button("Create account"):
        if not new_username or not new_password:
            st.warning("Please fill in all fields.")
        elif new_password != confirm_password:
            st.error("Passwords do not match.")
        else:
            success, message = register_user(new_username, new_password)

            if success:
                st.success(message)
                st.info("You can now log in from the Login tab.")
            else:
                st.error(message)