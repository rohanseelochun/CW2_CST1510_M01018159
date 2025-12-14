import streamlit as st
from app.data.db import connect_database
from app.data.incidents import *
from app.data.tickets import *
from app.data.datasets import *
from time import sleep


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

#Redirection if user is not logged in.
if not st.session_state.logged_in:
    st.error("Please log in to access the dashboard.")
    if st.button("Go to Login Page"):
        st.switch_page("Home.py")
        st.stop()

#Connecting the database.
conn = connect_database("DATA/intelligence_platform.db")

#Existing tabs.
tab_incidents, tab_tickets, tab_datasets = st.tabs(
    ["Incidents", "Tickets", "Datasets"]
)

#Incidents tab.
with tab_incidents:

    st.title("Cyber Incidents Dashboard")

    st.dataframe(get_all_incidents(conn), use_container_width=True)

    #Adding the incident.
    with st.form("new_incident"):
        timestamp = st.date_input("Timestamp")
        severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
        status = st.selectbox("Status", ["Open", "In Progress", "Resolved"])
        description = st.text_input("Description")
        category = st.text_input("Category")

        submitted = st.form_submit_button("Add Incident")

    if submitted:
        insert_incident(conn, timestamp, category, severity, status, description)
        st.success("✓ Incident added successfully!")
        conn.close()
        sleep(1)
        st.rerun()

    #Deleting the incident.
    with st.form("delete_incident"):
        delete_id = st.text_input("Enter Incident ID to Delete")
        delete_submit = st.form_submit_button("Delete Incident")

    if delete_submit and delete_id:
        delete_incident(conn, delete_id)
        st.success("✓ Incident deleted successfully!")
        conn.close()
        sleep(1)
        st.rerun()

    #Updating the incident.
    with st.form("update_incident"):
        incident_id = st.text_input("Enter Incident ID to Update")
        new_status = st.selectbox("New Status", ["Open", "In Progress", "Resolved"])
        update_submit = st.form_submit_button("Update Incident Status")

    if update_submit and incident_id:
        update_incident_status(conn, incident_id, new_status)
        st.success("✓ Incident status updated successfully!")
        conn.close()
        sleep(1)
        st.rerun()

    st.subheader("Incident Count by Type")
    st.dataframe(get_incidents_by_type_count(conn), use_container_width=True)

    st.subheader("High Severity Incidents by Status")
    st.dataframe(get_high_severity_by_status(conn), use_container_width=True)

    st.subheader("Incident Types with Minimum Cases")
    min_count = st.text_input("Enter Minimum Case Count", "5")
    st.dataframe(
        get_incident_types_with_many_cases(conn, int(min_count)),
        use_container_width=True
    )


#Tickets tab.
with tab_tickets:

    st.title("IT Tickets Dashboard")

    tickets = get_all_tickets(conn)
    tickets = tickets.rename(columns={"subject": "description"})
    st.dataframe(tickets, use_container_width=True)

    #Adding the ticket.
    with st.form("new_ticket"):
        ticket_id = st.text_input("Ticket ID")
        priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
        status = st.selectbox("Status", ["Open", "In Progress", "Resolved"])
        description = st.text_input("Description")
        assigned_to = st.text_input("Assigned To")
        created_at = st.date_input("Created At")

        submitted = st.form_submit_button("Add Ticket")

    if submitted and ticket_id:
        insert_ticket(conn, ticket_id, priority, description, status, assigned_to, created_at)
        st.success("✓ Ticket added successfully!")
        conn.close()
        sleep(1)
        st.rerun()

    #Deleting the ticket.
    with st.form("delete_ticket"):
        delete_id = st.text_input("Enter Ticket ID to Delete")
        delete_submit = st.form_submit_button("Delete Ticket")

    if delete_submit and delete_id:
        delete_ticket(conn, delete_id)
        st.success("✓ Ticket deleted successfully!")
        conn.close()
        sleep(1)
        st.rerun()

    #Updating the ticket.
    with st.form("update_ticket"):
        update_id = st.text_input("Enter Ticket ID to Update")
        new_status = st.selectbox("New Status", ["Open", "In Progress", "Resolved"])
        update_submit = st.form_submit_button("Update Ticket Status")

    if update_submit and update_id:
        update_ticket_status(conn, update_id, new_status)
        st.success("✓ Ticket updated successfully!")
        conn.close()
        sleep(1)
        st.rerun()

    st.subheader("High Priority Tickets by Status")
    st.dataframe(get_high_priority_tickets_by_status(conn), use_container_width=True)


#Datasets tab.
with tab_datasets:

    st.title("Datasets Metadata Dashboard")

    datasets = get_all_datasets(conn)
    datasets = datasets.rename(columns={"source": "uploaded_by"})
    datasets = datasets.drop(columns=["category", "file_size_mb"], errors="ignore")

    st.dataframe(datasets, use_container_width=True)

    #Add a dataset.
    with st.form("new_dataset"):
        name = st.text_input("Name")
        dataset_id = st.text_input("Dataset ID")
        record_count = st.number_input("Record Count", min_value=0)
        uploaded_by = st.text_input("Uploaded By")
        upload_date = st.date_input("Upload Date")

        submitted = st.form_submit_button("Add Dataset")

    if submitted:
        insert_dataset(conn, dataset_id, name, record_count, uploaded_by, upload_date)
        st.success("Dataset added successfully!")
        conn.close()
        sleep(1)
        st.rerun()

    #Deleting the dataset
    with st.form("delete_dataset"):
        delete_id = st.text_input("Enter Dataset ID to Delete")
        delete_submit = st.form_submit_button("Delete Dataset")

    if delete_submit and delete_id:
        delete_dataset(conn, delete_id)
        st.success("Dataset deleted successfully!")
        conn.close()
        sleep(1)
        st.rerun()

    #Updating the datasets.
    with st.form("update_dataset"):
        dataset_id = st.text_input("Enter Dataset ID to Update")
        new_record_count = st.number_input("Enter new Record Count", min_value=0)
        update_submit = st.form_submit_button("Update Dataset Rows")

    if update_submit and dataset_id:
        update_dataset_num_rows(conn, dataset_id, new_record_count)
        st.success("Dataset updated successfully!")
        conn.close()
        sleep(1)
        st.rerun()