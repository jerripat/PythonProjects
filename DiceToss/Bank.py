import sqlite3
import random
cust_id = random.randint(1, 10000)  # Generate a random customer ID

def get_deposit(cust_id):
    """Prompt the user for a valid deposit amount."""
    try:
        deposit = float(input("Enter deposit amount: "))
        return deposit
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        # pass cust_id again so recursion works
        return get_deposit(cust_id)
deposit = get_deposit(cust_id)
print(f"✅ Deposit of ${deposit} added for customer {cust_id}.")
if __name__ == "__main__":
    get_deposit(cust_id)