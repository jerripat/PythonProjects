from tkinter import *
import requests
import json


tk = Tk()

tk.title("My Portfolio")
tk.geometry("500x500")
tk.config(bg="teal")


def my_portfolio():
    api_request = requests.get(
        "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=55751a9b-f3f9-4cfb-82e3-ff30a2a345bd"
    )
    api = json.loads(api_request.content)


coins = [
    {"symbol": "BTC", "amount_owned": 2, "pri_per_coin": 3200},
    {"symbol": "ETH", "amount_owned": 2, "pri_per_coin": 3200},
    {"symbol": "LTC", "amount_owned": 20, "pri_per_coin": 320},
]

for coin in coins:
    if api["data"][i]["symbol"] == coin["symbol"]:
        total_paid = coin["amount_owned"] * coin["price_per_coin"]
        current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
        pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
        total_pl_coin = pl_percoin * coin["amount_owned"]

        total_pl = total_pl + total_pl_coin

        print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
        print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
        print("Number Of Coin:", coin["amount_owned"])
        print("Total Amount Paid:", "$0:.2f".format(total_paid))
        print("Current Value:", "$0:.2f".format(current_value))
        print("P/L Per Coin:", "${0:.2f}".format(pl_percoin))
        print("Total P/L with coin:", "$0:.2f".format(total_pl_coin))
        print("--------------------")

    print("Total P/L for Portfolio:", "$0:.2f".format(total_pl))

name = Label(tk, text="Bitcoin", bg="teal", fg="yellow")
name.grid(row=0, column=0, columnspan=3)

price = Label(tk, text="Price", bg="teal", fg="yellow")
price.grid(row=0, columnn=1, columnspan=3)

no_coins = Label(tk, text="Coins Owned", bg="teal", fg="yellow")
no_coins.grid(row=0, column=2, columnspan=3)

amount_paid = Label(tk, text="Total Amount Paid", bg="teal", fg="yellow")
amount_paid.grid(row=0, column=3, columnspan=3)

current_val = Label(tk, text="Current Value", bg="teal", fg="yellow")
current_val.grid(row=0, column=4, columnspan=3)

pl_coin = Label(tk, text="P/L Per Coin", bg="teal", fg="yellow")
pl_coin.grid(row=0, column=5, columnspan=3)

total_pl = Label(tk, text="Total P/L", bg="teal", fg="yellow")
totalpl.grid(row=0, column=6, columnspan=3)

tk.mainloop()
print("Program Completed")
