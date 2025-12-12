import streamlit as st
import pandas as pd

st.set_page_config(page_title="🛡️ Cyber Incidents", page_icon="🛡️", layout="wide")

# --- Guard: ensure auth state exists & user is logged in ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if not st.session_state.logged_in:
    st.error("You must be logged in to view this page.")
    if st.button("Go to Login"):
        st.switch_page("Home.py")
    st.stop()

# --- In-memory incident store for Week 9 learning (we'll swap to DB later) ---
if "incidents" not in st.session_state:
    st.session_state.incidents = []  # list of dicts: {"title":..., "severity":..., "status":...}

st.title("🛡️ Cyber Incidents Dashboard")
st.caption(f"Signed in as **{st.session_state.username}**")

# --- READ: display incidents ---
df = pd.DataFrame(st.session_state.incidents)
if not df.empty:
    st.subheader("All Incidents")
    st.dataframe(df, use_container_width=True)
else:
    st.info("No incidents yet. Add one with the form below.")

st.divider()

# --- CREATE: add a new incident via a form ---
with st.form("new_incident"):
    st.subheader("Add New Incident")
    title = st.text_input("Incident Title")
    severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
    status = st.selectbox("Status", ["Open", "In Progress", "Resolved"])
    submitted = st.form_submit_button("Add Incident")

    if submitted:
        if not title:
            st.warning("Please provide a title.")
        else:
            st.session_state.incidents.append(
                {"title": title, "severity": severity, "status": status}
            )
            st.success("✓ Incident added successfully!")
            st.rerun()  # refresh the table

st.divider()
if st.button("Log out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.info("You have been logged out.")
    st.switch_page("Home.py")