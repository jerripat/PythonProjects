from tkinter import *
import requests
import json


tk = Tk()

tk.title("My Portfolio")
tk.geometry("750x500")
tk.config(bg="#08215e")


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
            current_value = (
                coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
            )
            pl_percoin = (
                api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
            )
            total_pl_coin = pl_percoin * coin["amount_owned"]

            total_pl = total_pl + total_pl_coin

        #     print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
        #     print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
        #     print("Number Of Coin:", coin["amount_owned"])
        #     print("Total Amount Paid:", "$0:.2f".format(total_paid))
        #     print("Current Value:", "$0:.2f".format(current_value))
        #     print("P/L Per Coin:", "${0:.2f}".format(pl_percoin))
        #     print("Total P/L with coin:", "$0:.2f".format(total_pl_coin))
        #     print("--------------------")

        # print("Total P/L for Portfolio:", "$0:.2f".format(total_pl))


name = Label(tk, text="Bitcoin ", bg="#08215e", fg="yellow", font=("Arial", 12))
name.grid(row=0, column=0, sticky=N + S + E + W)


price = Label(tk, text="Price ", bg="#08215e", fg="yellow", font=("Arial", 12))
price.grid(row=0, column=1, sticky=N + S + E + W)

no_coins = Label(
    tk, text="Coins Owned ", bg="#08215e", fg="yellow", font=("Arial", 12)
)
no_coins.grid(row=0, column=2, sticky=N + S + E + W)

amount_paid = Label(
    tk, text="Total Paid ", bg="#08215e", fg="yellow", font=("Arial", 12)
)
amount_paid.grid(row=0, column=3, sticky=N + S + E + W)

current_val = Label(
    tk, text="Current Value ", bg="#08215e", fg="yellow", font=("Arial", 12)
)
current_val.grid(row=0, column=4, sticky=N + S + E + W)

pl_coin = Label(
    tk, text="P/L Per Coin ", bg="#08215e", fg="yellow", font=("Arial", 12)
)
pl_coin.grid(row=0, column=5, sticky=N + S + E + W)

total_pl = Label(tk, text="Total P/L", bg="#08215e", fg="yellow", font=("Arial", 12))
total_pl.grid(row=0, column=6, sticky=N + S + E + W)

tk.mainloop()
print("Program Completed")
