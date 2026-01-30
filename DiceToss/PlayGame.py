import random
import _deposits
import Customers
point = 0
fname = Customers.customerData().fname
lname = Customers.customerData().lname
wager = _deposits.add_wager(Customers.customerData(),3, initial_balance=0.0, wager=100.0)

