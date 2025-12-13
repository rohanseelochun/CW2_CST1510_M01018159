import pandas as pd

def get_all_tickets(conn):
    return pd.read_sql_query("SELECT * FROM it_tickets", conn)


def insert_ticket(conn, ticket_id, priority, subject, status, assigned_to, created_at):
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO it_tickets
        (ticket_id, priority, status, subject, created_date, assigned_to)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (ticket_id, priority, status, subject, created_at, assigned_to)
    )
    conn.commit()
    return cursor.lastrowid


def delete_ticket(conn, ticket_id):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM it_tickets WHERE ticket_id = ?",
        (ticket_id,)
    )
    conn.commit()
    return cursor.rowcount


def update_ticket_status(conn, ticket_id, new_status):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE it_tickets SET status = ? WHERE ticket_id = ?",
        (new_status, ticket_id)
    )
    conn.commit()
    return cursor.rowcount


def get_high_priority_tickets_by_status(conn):
    query = """
    SELECT status, COUNT(*) AS count
    FROM it_tickets
    WHERE priority = 'High'
    GROUP BY status
    ORDER BY count DESC
    """
    return pd.read_sql_query(query, conn)