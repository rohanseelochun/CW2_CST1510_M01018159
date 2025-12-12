from pathlib import Path
import pandas as pd

def create_users_table(conn):
    """Create users table."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        )
    """)
    conn.commit()

def create_cyber_incidents_table(conn):
    """Create cyber_incidents table."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cyber_incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            incident_type TEXT,
            severity TEXT,
            status TEXT,
            description TEXT,
            reported_by TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (reported_by) REFERENCES users(username)
            )
        """)
    conn.commit()
    print("Successfully created Cyber Incidents table.")
    pass

def create_datasets_metadata_table(conn):
    """Create datasets_metadata table."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS datasets_metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dataset_name TEXT NOT NULL,
            category TEXT,
            source TEXT,
            last_updated TEXT,
            record_count INTEGER,
            file_size_mb REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    conn.commit()
    print("Successfully created Datasets Metadata table.")
    pass

def create_it_tickets_table(conn):
    """Create it_tickets table."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS it_tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id TEXT UNIQUE NOT NULL,
            priority TEXT,
            status TEXT,
            category TEXT,
            subject TEXT NOT NULL,
            description TEXT,
            created_date TEXT,
            resolved_date TEXT,
            assigned_to TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    conn.commit()
    print("Successfully created It Tickets table.")
    pass

#Load CSV to Table
def load_csv_to_table(conn, csv_path, table_name):
    """
    Load a CSV file into a database table using pandas.

    TODO: Implement this function.

    Args:
        conn: Database connection
        csv_path: Path to CSV file
        table_name: Name of the target table

    Returns:
        int: Number of rows loaded
    """
    # TODO: Check if CSV file exists
    if not csv_path.exists():
        print(f"⚠️ File not found: {csv_path}")
        return 0

    # TODO: Read CSV using pandas.read_csv()
    df = pd.read_csv(csv_path)

    # TODO: Use df.to_sql() to insert data
    # Parameters: name=table_name, con=conn, if_exists='append', index=False
    df.to_sql(name=table_name, con=conn, if_exists='append', index=False)

    # TODO: Print success message and return row count
    row_count = len(df)
    print(f"Loaded {row_count} rows into '{table_name}' from {csv_path}")
    return row_count

#Load All CSV
def load_all_csv_data(conn):
    cursor = conn.cursor()
    tables = ["cyber_incidents", "datasets_metadata", "it_tickets"]
    total_rows = 0
    
    for table in tables:
        cursor.execute(f"SELECT COUNT (*) FROM {table}")
        count = cursor.fetchone()[0]
        total_rows += count
    return total_rows

def create_all_tables(conn):
    """Create all tables."""
    create_users_table(conn)
    create_cyber_incidents_table(conn)
    create_datasets_metadata_table(conn)
    create_it_tickets_table(conn)