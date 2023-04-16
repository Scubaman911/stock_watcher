from typing import Dict, List, Optional
from pprint import pprint
from stock_builder import StockBuilder, Stock, yf
# currentPrice
# open
# previousClose

ticker_list = ["RIO.L", "RIVN", "^FTSE"]

def main():
    stocks: List[Stock] = []
    for stock in ticker_list:
        built = StockBuilder(stock)
        built.collate_daily_price_data()
        stocks.append(built.stock)

    for built_stock in stocks:
        pprint(built_stock.daily_price_data)

def news():
    rio = yf.Ticker(ticker_list[0])
    for story in rio.news:
        pprint(story.get("title"))

    print("")

    rivian = yf.Ticker("RIVN")
    for story in rivian.news:
        pprint(story.get("title"))

    

if __name__ == "__main__":
    news()
