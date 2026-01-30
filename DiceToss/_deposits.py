import Customers
import _deposits
import sqlite3
fname = Customers.customerData().fname
lname = Customers.customerData().lname
wager = int(input(f'Enter your wager for {fname} {lname}: '))

try:
    deposits.add_wager(Customers.customerData().cust_id,  wager=wager)
    print(f'�� Added wager for {fname} {lname} with wager={wager}')

except sqlite3.IntegrityError:
    print(f'Error: Wager for {fname} {lname} already exists.')

connection = sqlite3.connect('bank.db')
cursor = connection.cursor()
