# customers.py
import sqlite3
import _deposits  # expects deposits.add_wager(cust_id, initial_balance=0.0, wager=0.0)

DB_PATH = "_customers.db"

class Customer:
    def __init__(self, fname: str, lname: str, cust_id: int):
        self.fname = fname
        self.lname = lname
        self.cust_id = cust_id

def init_db():
    """Create customers table if it doesn't exist."""
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,         -- internal PK
                fname TEXT NOT NULL,
                lname TEXT NOT NULL,
                cust_id INTEGER UNIQUE NOT NULL -- public id used to join with wagers
            )
            """
        )
        conn.commit()

def create_customer(fname: str, lname: str) -> Customer:
    """
    Insert a new customer and return the Customer object.
    We use SQLite's internal rowid as the cust_id so it's guaranteed unique.
    """
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        # Insert first to get the auto id, then store it again as cust_id
        cur.execute("INSERT INTO customers (fname, lname, cust_id) VALUES (?, ?, -1)", (fname, lname))
        new_id = cur.lastrowid  # this is the internal PK we can use as cust_id

        # Update the same row to set cust_id = new_id (keeps them in sync and unique)
        cur.execute("UPDATE customers SET cust_id = ? WHERE id = ?", (new_id, new_id))
        conn.commit()

    return Customer(fname, lname, new_id)

def customerData():
    init_db()
    fname = input("Enter customer's first name: ").strip()
    lname = input("Enter customer's last name: ").strip()

    customer = create_customer(fname, lname)

    # Create/initialize their wager row in bank.db (wagers table).
    # Your deposits.add_wager should no-op if the column/table already exists.
   _deposits.add_wager(customer.cust_id, initial_balance=0.0, wager=0.0)

    print(f"✅ Created customer {customer.fname} {customer.lname} with cust_id={customer.cust_id}")
    return customer


