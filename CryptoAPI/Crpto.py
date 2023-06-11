# This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
parameters = {"start": "1", "limit": "5", "convert": "USD"}
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "55751a9b-f3f9-4cfb-82e3-ff30a2a345bd",
}
# Create a session"https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=55751a9b-f3f9-4cfb-82e3-ff30a2a345bd"
# xdg-open 
session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
