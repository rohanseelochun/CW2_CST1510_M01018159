import pandas as pd


#Get all tickets from the database.
def get_all_tickets(conn):
    return pd.read_sql_query("SELECT * FROM it_tickets", conn)


#Add a new ticket.
def insert_ticket(conn, ticket_id, priority, subject, status, assigned_to, created_at):
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO it_tickets
        (ticket_id, priority, status, subject, created_date, assigned_to)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (ticket_id, priority, status, subject, created_at, assigned_to)
    )
    conn.commit()
    return cursor.lastrowid


#Delete a ticket using its ID.
def delete_ticket(conn, ticket_id):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM it_tickets WHERE ticket_id = ?",
        (ticket_id,)
    )
    conn.commit()
    return cursor.rowcount


#Update the status of the ticket.
def update_ticket_status(conn, ticket_id, new_status):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE it_tickets SET status = ? WHERE ticket_id = ?", (new_status, ticket_id)
    )
    conn.commit()
    return cursor.rowcount


#Count the high priority tickets that are grouped in the status.
def get_high_priority_tickets_by_status(conn):
    query = """
    SELECT status, COUNT(*) AS count
    FROM it_tickets
    WHERE priority = 'High'
    GROUP BY status
    ORDER BY count DESC
    """
    return pd.read_sql_query(query, conn)


#Count the tickets that are grouper by priority.
def get_tickets_by_priority_count(conn):
    query = """
    SELECT priority, COUNT(*) AS count
    FROM it_tickets
    GROUP BY priority
    ORDER BY count DESC
    """
    return pd.read_sql_query(query, conn)