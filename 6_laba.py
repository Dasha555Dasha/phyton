import json
import sqlite3


def create_tables_from_json(file_path):
    with open(file_path) as file:
        data = json.load(file)

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    for table_name, fields in data.items():
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ("

        for field_name, field_type in fields.items():
            query += f"{field_name} {field_type}, "

        query = query.rstrip(", ") + ")"
        cursor.execute(query)

    conn.commit()
    conn.close()
