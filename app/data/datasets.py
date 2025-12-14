import pandas as pd

#Inserting dataset.
def insert_dataset(conn, dataset_id, name, record_count, uploaded_by, upload_date):
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO datasets_metadata
        (id, dataset_name, record_count, source, last_updated)
        VALUES (?, ?, ?, ?, ?)
        """,
        (dataset_id, name, record_count, uploaded_by, upload_date)
    )
    conn.commit()
    return cursor.lastrowid


#Reading dataset.
def get_all_datasets(conn):
    return pd.read_sql_query("SELECT * FROM datasets_metadata", conn)


# Deleting dataset.
def delete_dataset(conn, dataset_id):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM datasets_metadata WHERE id = ?",
        (dataset_id,)
    )
    conn.commit()
    return cursor.rowcount


#Updating dataset.
def update_dataset_num_rows(conn, dataset_id, new_num_rows):
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE datasets_metadata
        SET record_count = ?
        WHERE id = ?
        """,
        (new_num_rows, dataset_id)
    )
    conn.commit()
    return cursor.rowcount