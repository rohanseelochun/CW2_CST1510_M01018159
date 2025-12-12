import pandas as pd

#Insert Datasets
def insert_datasets(conn, dataset_id, name, rows, columns, uploaded_by, upload_date):
    """
    Insert a new cyber incident into the database.

    TODO: Implement this function following the register_user() pattern.

    Args:
        conn: Database connection
        date: Incident date (YYYY-MM-DD)
        incident_type: Type of incident
        severity: Severity level
        status: Current status
        description: Incident description
        reported_by: Username of reporter (optional)

    Returns:
        int: ID of the inserted incident
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO cyber_incidents (dataset_id, name, rows, columns, uploaded_by, upload_date)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (dataset_id, name,rows, columns, uploaded_by, upload_date))
    conn.commit()
    return cursor.lastrowid
pass

def get_all_datasets(conn):
    """
    Retrieve all incidents from the database.

    TODO: Implement using pandas.read_sql_query()

    Returns:
        pandas.DataFrame: All incidents
    """
    return pd.read_sql_query("SELECT * FROM cyber_incidents", conn)
pass

#Update Datasets Rows
def update_datasets_rows(conn, dataset_id, new_rows):
    """
    Update the status of an incident.

    TODO: Implement UPDATE operation.
    """
    cursor = conn.cursor()
    cursor.execute(
    """
    UPDATE datasets_metadata SET rows = ? WHERE dataset_id = ?
    """, (new_rows, dataset_id))
    conn.commit()
    return cursor.rowcount
pass

#Delete Datasets
def delete_datasets(conn, dataset_id):
    """
    Delete an incident from the database.

    TODO: Implement DELETE operation.
    """
    cursor = conn.cursor()
    cursor.execute(
    """
    DELETE FROM datasets_metadata WHERE dataset_id = ?
    """, (dataset_id,))
    conn.commit()
    return cursor.rowcount
pass