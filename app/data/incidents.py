import pandas as pd


#Get the number of incidents for each incident_type
def get_incidents_by_type_count(conn):
    query = """
    SELECT incident_type, COUNT(*) as count
    FROM cyber_incidents
    GROUP BY incident_type
    ORDER BY count DESC
    """
    return pd.read_sql_query(query, conn)


#Get the high severity incidents grouped by status.
def get_high_severity_by_status(conn):
    query = """
    SELECT status, COUNT(*) as count
    FROM cyber_incidents
    WHERE severity = 'High'
    GROUP BY status
    ORDER BY count DESC
    """
    return pd.read_sql_query(query, conn)



def get_incident_types_with_many_cases(conn, min_count=5):
    query = """
    SELECT incident_type, COUNT(*) as count
    FROM cyber_incidents
    GROUP BY incident_type
    HAVING COUNT(*) > ?
    ORDER BY count DESC
    """
    return pd.read_sql_query(query, conn, params=(min_count,))



#Add a new incident.
def insert_incident(conn, timestamp, category, severity, status, description):
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO cyber_incidents
        (date, incident_type, severity, status, description)
        VALUES (?, ?, ?, ?, ?)
        """,
        (timestamp, category, severity, status, description)
    )
    conn.commit()
    return cursor.lastrowid


#Get all the incidents from the database.
def get_all_incidents(conn):
    return pd.read_sql_query(
        "SELECT * FROM cyber_incidents",
        conn
    )


#Update the status of the incident.
def update_incident_status(conn, incident_id, new_status):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE cyber_incidents SET status = ? WHERE id = ?",
        (new_status, incident_id)
    )
    conn.commit()
    return cursor.rowcount


#Delete the incident by making use of its ID.
def delete_incident(conn, incident_id):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM cyber_incidents WHERE id = ?",
        (incident_id,)
    )
    conn.commit()
    return cursor.rowcount