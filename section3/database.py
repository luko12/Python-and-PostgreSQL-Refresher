import sqlite3

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries1 (content TEXT, date TEXT);"
        )

def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            "INSERT INTO entries1 VALUES (?, ?);", (entry_content, entry_date)
        )

def get_entries():
    cursor = connection.execute(
        "SELECT * FROM entries1;"
    )
    return cursor
    