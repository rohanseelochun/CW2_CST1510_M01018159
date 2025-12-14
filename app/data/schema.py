from pathlib import Path
import pandas as pd


#Create users table.
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


#Create cyber_incidents table.
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
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    conn.commit()
    print("Successfully created Cyber Incidents table.")
    pass


#Create the datasets_metadata table.
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


#Create the it_tickets table.
def create_it_tickets_table(conn):
    """Create it_tickets table."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS it_tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id TEXT UNIQUE NOT NULL,
            priority TEXT,
            status TEXT,
            subject TEXT NOT NULL,
            created_date TEXT,
            assigned_to TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    conn.commit()
    print("Successfully created It Tickets table.")
    pass


#Load CSV file into the database table.
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
    #Check if CSV file exists
    if not csv_path.exists():
        print(f"File not found: {csv_path}")
        return 0

    #Read CSV using pandas.read_csv()
    df = pd.read_csv(csv_path)

    if table_name == "cyber_incidents":
        df = df.rename(columns={
            "timestamp": "date",
            "category": "incident_type"
        })
        df = df.drop(columns=["incident_id"])

    elif table_name == "datasets_metadata":
        df = df.rename(columns={
            "name": "dataset_name",
            "rows": "record_count",
            "upload_date": "last_updated",
            "uploaded_by": "source"
        })
        df = df.drop(columns=["dataset_id","columns"])

    elif table_name == "it_tickets":
        df = df.rename(columns={
            "created_at": "created_date",
            "description": "subject"
        })
        df = df.drop(columns=["resolution_time_hours"])

    #Used to clear the existing data before inserting.
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name}")
    conn.commit()

    #Use df.to_sql() to insert data
    # Parameters: name=table_name, con=conn, if_exists='append', index=False
    df.to_sql(name=table_name, con=conn, if_exists='append', index=False)

    #Print success message and return row count
    row_count = len(df)
    print(f"Loaded {row_count} rows into '{table_name}' from {csv_path}")
    return row_count


#Load All CSV files into the database.
DATA_DIR = Path("DATA")

def load_all_csv_data(conn):
    tables = {
        "cyber_incidents": DATA_DIR / "cyber_incidents.csv",
        "datasets_metadata": DATA_DIR / "datasets_metadata.csv",
        "it_tickets": DATA_DIR / "it_tickets.csv",
    }

    total_rows = 0

    for table_name, csv_file in tables.items():
        rows = load_csv_to_table(conn, csv_file, table_name)
        total_rows += rows

    return total_rows


#Create all database tables.
def create_all_tables(conn):
    """Create all tables."""
    create_users_table(conn)
    create_cyber_incidents_table(conn)
    create_datasets_metadata_table(conn)
    create_it_tickets_table(conn)