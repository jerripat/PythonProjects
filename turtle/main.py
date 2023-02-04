# from turtle import Turtle, Screen
# from tkinter import *
# #tk =Tk()
# tim = Turtle()
# tim.shape('turtle')
# tim.color('green')
# tim.forward(100)
# #tk.geometry('300x300')
# my_screen = Screen()
# my_screen.bgcolor='blue'
# my_screen.exitonclick()

from prettytable import PrettyTable as pt
import sqlite3
from prettytable import from_db_cursor
conn=sqlite3.connect('measurementdb.db')
cursor = conn.cursor()


table = pt()
table.add_column(
    "Weights and Measures", ["Weight", "Distance","temperature"])

table.add_column("Units", ["lb - kg", "inch - millimeters", "Farenheit - Celcius"])
table.align = "l"
table.add_row([100, 200])
print(table)
