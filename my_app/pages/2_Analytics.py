import streamlit as st
from app.data.db import connect_database

from app.data.incidents import (
    get_incidents_by_type_count,
    get_high_severity_by_status
)

from app.data.tickets import (
    get_high_priority_tickets_by_status,
    get_tickets_by_priority_count
)

from app.data.datasets import get_all_datasets


st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
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


#Connection to the database.
conn = connect_database("DATA/intelligence_platform.db")

st.title("📊 System Analytics Dashboard")
st.write("This page presents analytical insights derived from incidents, tickets, and datasets.")


#Incidents analytics.
st.header("🚨 Incident Analytics")

st.subheader("Incident Count by Type")
incident_type_count = get_incidents_by_type_count(conn)

st.bar_chart(
    incident_type_count.set_index("incident_type")["count"]
)

st.subheader("High Severity Incidents by Status")
high_severity = get_high_severity_by_status(conn)

st.bar_chart(
    high_severity.set_index("status")["count"]
)

st.divider()

#Ticket analytics.
st.header("🎫 Ticket Analytics")

st.subheader("Tickets by Priority")
tickets_by_priority = get_tickets_by_priority_count(conn)

st.bar_chart(
    tickets_by_priority.set_index("priority")["count"]
)

st.subheader("High Priority Tickets by Status")
high_priority = get_high_priority_tickets_by_status(conn)

if high_priority.empty:
    st.info("No high priority tickets found.")
else:
    st.bar_chart(
        high_priority.set_index("status")["count"]
    )

st.divider()

conn.close()