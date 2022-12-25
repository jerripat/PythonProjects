import yfinance as yf

STK = input("Enter share name : ")
Share = yf.Ticker(STK).info
market_price = Share["regularMarketPrice"]
print(market_price)
