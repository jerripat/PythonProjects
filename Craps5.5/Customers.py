import sqlite3
import random

class Customer:
    def __init__(self, cust_id, name, address, email, phone_number):
        self.cust_id = cust_id
        self.name = name
        self.address = address
        self.email = email
        self.phone_number = phone_number

    def insert_into_db(self):
        """Create table (if not exists) and insert customer data"""
        conn = sqlite3.connect('customer_db.db')
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                cust_id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT,
                email TEXT,
                phone_number TEXT
            )
        """)
        c.execute(
            "INSERT INTO customers (cust_id, name, address, email, phone_number) VALUES (?, ?, ?, ?, ?)",
            (self.cust_id, self.name, self.address, self.email, self.phone_number)
        )
        conn.commit()
        conn.close()
        print(f"✅ Customer '{self.name}' added successfully with ID: {self.cust_id}")

# ------------------------------
# Example usage
# ------------------------------
if __name__ == "__main__":
    # Generate a random ID
    cust_id = random.randint(1000, 9999)

    # Prompt user for customer info
    name = input("Enter customer's name: ")
    address = input("Enter address: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")

    # Create and save customer
    customer = Customer(cust_id, name, address, email, phone)
    customer.insert_into_db()

def get_name(cust_id):
    """Get customer name from ID"""
    conn = sqlite3.connect('customer_db.db')
    c = conn.cursor()
    c.execute("SELECT name FROM customers WHERE cust_id=?", (cust_id,))
    result = c.fetchone()
    conn.close()
    print(f"Customer with ID '{cust_id}' is: {result[0]}")
    return result[0]  + " " + result[1] if result else None

get_name(9482)
