from tkinter import *


tk = Tk()

# tk.title("Coin Market Cap")
# tk.geometry("500x500")
# tk.config(bg="teal")


def my_portfolio():
    tk.title("My Portfolio")
    tk.geometry("500x500")
    tk.config(bg="teal")
    tk.destroy()
    portfolio()


api_request = requests.get(
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=55751a9b-f3f9-4cfb-82e3-ff30a2a345bd"
)
api = json.loads(api_request.content)


coins = ["BTC", "ETH", "USDT", "BNB", "USDC"]

for i, coin in itertools.product(range(5), coins):
    if api["data"][i]["symbol"] == coin["symbol"]:
        total_paid = coin["amount_owned"] * coin["prive_per_coin"]
        current_value = coin["amount_owned"] * print(
            "{0:.2f}".format(api["data"][i]["quote"]["USD"]["price"])
        )
        pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
        total_pl_coin = pl_percoin * coin["amount_owned"]

        total_pl_coin = total_pl + total_pl_coin

        print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
        print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
        print("Number Of Coin:", coin["amount_owned"])
        print("Total Amount Paid:", "$0:.2f".format(total_paid))
        print("Current Value:", "$0:.2f".format(current_value))
        print("P/L Per Coin:", "${0:.2f}".format(pl_percoin))
        print("Total P/L:", "$0:.2f".format(total_pl_coin))
        print("--------------------")

    print("Total P/L for Portfolio:", "$0:.2f".format(total_pl))

name = Label(tk, text="Bitcoin", bg="teal", fg="yellow")
name.grid(row=0, colun=0, columnspan=3)

print("Program Completed")
