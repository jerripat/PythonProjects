import sqlite3
import random


def create_customer():
    cust_id = createCustNum()
    name = input("Enter customer's name: ")


def createCustNum():
    return random.randint(10,999)

