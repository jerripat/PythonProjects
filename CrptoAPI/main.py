from tkinter import *
import requests
import json


tk = Tk()

tk.title("My Portfolio")
tk.geometry("750x500")
tk.config(bg="#08215e")


def my_portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=55751a9b-f3f9-4cfb-82e3-ff30a2a345bd")
    api = json.loads(api_request.content)

    coins = [
        {"symbol": "BTC", "amount_owned": 2, "pri_per_coin": 3200},
        {"symbol": "ETH", "amount_owned": 2, "pri_per_coin": 3200},
        {"symbol": "LTC", "amount_owned": 20, "pri_per_coin": 320},
    ]
    total_pl = 0
    coin_row = 1
    
    for i in range(len(api["data"])):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                
                total_paid = coin["amount_owned"] * coin["pri_per_coin"]
                
                current_value = (coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
            )
                pl_percoin = (api["data"][i]["quote"]["USD"]["price"] - coin["pri_per_coin"]
            )
                total_pl_coin = pl_percoin * coin["amount_owned"]

                total_pl = total_pl + total_pl_coin

        name = Label(tk, text=api["data"][i]["symbol"], bg="#08215e", fg="yellow", font=("Arial", 12))
        name.grid(row=0, column=0, sticky=N + S + E + W)


        price = Label(tk, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="#08215e", fg="yellow", font=("Arial", 12))
        price.grid(coin_row, column=1, sticky=N + S + E + W)

        no_coins = Label(tk, text=coin["amount_owned"], bg="#08215e", fg="yellow", font=("Arial", 12))
        no_coins.grid(coin_row, column=2, sticky=N + S + E + W)

        amount_paid = Label(tk, text="${0:.2f}".format(total_paid), bg="#08215e", fg="yellow", font=("Arial", 12))
        
        amount_paid.grid(coin_row, column=3, sticky=N + S + E + W)

        current_val = Label(tk, text="$0:.2f".format(current_value), bg="#08215e", fg="yellow", font=("Arial", 12))
        current_val.grid(coin_row, column=4, sticky=N + S + E + W)

        pl_coin = Label(tk, text="${0:.2f}".format(pl_percoin), bg="#08215e", fg="yellow", font=("Arial", 12))
        pl_coin.grid(coin_row, column=5, sticky=N + S + E + W)

        total_pl = Label(tk, text= "$0:.2f".format(total_pl_coin), bg="#08215e", fg="yellow", font=("Arial", 12))
        total_pl.grid(coin_row, column=6, sticky=N + S + E + W)

        coin_row = coin_row + 1
        
    print("Total P/L for Portfolio:", "$0:.2f".format(total_pl))
    
my_portfolio()

tk.mainloop()

print("Program Completed")
