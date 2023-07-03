text = "apple,banana,grape,orange"
split_text = text.split(",")
print(split_text)

text = "apple,,,,banana,,grape,orange,,,,,"
split_text = text.split(",")
filtered_text = [word for word in split_text if word]
print(filtered_text)

import sqlite3

def insert_items_into_database(items, database_name, table_name):
    # Connect to the database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (item TEXT)")

    # Loop through the items and insert them into the table
    for item in items:
        cursor.execute(f"INSERT INTO {table_name} (item) VALUES (?)", (item,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Example usage
my_items = ["Apple", "Banana", "Orange"]
database = "mydatabase.db"
table = "mytable"
insert_items_into_database(my_items, database, table)

