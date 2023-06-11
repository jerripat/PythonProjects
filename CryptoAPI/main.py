import itertools
import requests
import json

api_request = requests.get(
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=55751a9b-f3f9-4cfb-82e3-ff30a2a345bd"
)

api = json.loads(api_request.content)

coins =['BTC', 'ETH', 'USDT', 'BNB', 'USDC']

for i, coin in itertools.product(range(5), coins):
    if coin in api["data"][i]["symbol"] == coin:
        print(api["data"][i]["symbol"])
        print("{0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
        print('----------')
            
