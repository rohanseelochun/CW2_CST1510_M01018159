import streamlit as st

# Page config must be the first Streamlit call
st.set_page_config(page_title="🔐 Login / Register", page_icon="🔐", layout="centered")

# --- Initialize session state keys ---
if "users" not in st.session_state:
    # Teaching-only in-memory "database": {username: password}
    st.session_state.users = {}
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "role" not in st.session_state:
    st.session_state.role = "user"  # default role for now

st.title("🔐 Welcome")

# If already logged in, offer direct navigation and don’t show tabs again
if st.session_state.logged_in:
    st.success(f"Already logged in as **{st.session_state.username}** (role: {st.session_state.role}).")
    if st.button("Go to Dashboard ➜", type="primary"):
        st.switch_page("pages/1_Dashboard.py")
    st.stop()

# --- Tabs: Login / Register ---
tab_login, tab_register = st.tabs(["Login", "Register"])

# ------- LOGIN TAB -------
with tab_login:
    st.subheader("Login")
    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")

    if st.button("Log in", type="primary"):
        # Teaching-only check against in-memory dict
        users = st.session_state.users
        if login_username in users and users[login_username] == login_password:
            st.session_state.logged_in = True
            st.session_state.username = login_username
            st.session_state.role = "user"  # or set based on username if you want
            st.success(f"Welcome back, {login_username}! 🎉")
            st.switch_page("pages/1_Dashboard.py")
        else:
            st.error("Invalid username or password.")

# ------- REGISTER TAB (in-memory) -------
with tab_register:
    st.subheader("Register")
    new_username = st.text_input("Choose a username", key="register_username")
    new_password = st.text_input("Choose a password", type="password", key="register_password")
    confirm_password = st.text_input("Confirm password", type="password", key="register_confirm")

    if st.button("Create account"):
        if not new_username or not new_password:
            st.warning("Please fill in all fields.")
        elif new_password != confirm_password:
            st.error("Passwords do not match.")
        elif new_username in st.session_state.users:
            st.error("Username already exists. Choose another one.")
        else:
            # Teaching-only: store plaintext in memory (we’ll replace with DB + hashing later)
            st.session_state.users[new_username] = new_password
            st.success("Account created! You can now log in from the Login tab.")
            st.info("Tip: go to the Login tab and sign in with your new account.")