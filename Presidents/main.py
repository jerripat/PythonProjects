def read_president_text(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File not found.")
        return None
    except IOError:
        print("An error occurred while reading the file.")
        return None

file_path = 'us_presidents.txt'  # Replace with the actual file path
president_text = read_president_text(file_path)
if president_text is not None:
    print(president_text)


import sqlite3

def save_president_text_to_db(file_path, db_file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS presidents (text TEXT)")
        cursor.execute("INSERT INTO presidents (text) VALUES (?)", (text,))
        conn.commit()
        conn.close()
        
        print("Data saved to the database successfully.")
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("An error occurred while reading the file.")


file_path = 'us_presidents.txt'  # Replace with the actual file path
db_file_path = 'presidents.db'   # Replace with the desired database file path

save_president_text_to_db(file_path, db_file_path)

import sqlite3

def save_text_to_db(file_path, db_file_path):
    try:
        with open(file_path, 'r') as file:
            text_data = file.read()
        
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS data (text TEXT)")
        cursor.execute("INSERT INTO data (text) VALUES (?)", (text_data,))
        conn.commit()
        conn.close()
        
        print("Data saved to the database successfully.")
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("An error occurred while reading the file.")

# Example usage
file_path = 'data.txt'          # Replace with the actual file path
db_file_path = 'data.db'        # Replace with the desired database file path

save_text_to_db(file_path, db_file_path)
