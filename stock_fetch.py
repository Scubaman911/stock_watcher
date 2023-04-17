from typing import Dict, List, Optional
from pprint import pprint
from stock_builder import StockBuilder, Stock, yf
from datetime import datetime
# currentPrice
# open
# previousClose

ticker_list = ["RIO.L", "RIVN", "^FTSE"]

def main():
    stocks: List[Stock] = []
    for stock in ticker_list:
        built = StockBuilder(stock)
        built.collate_daily_price_data()
        built.collate_news_data()
        stocks.append(built.stock)

    for built_stock in stocks:
        print(f"*** Info for {built_stock.ticker}! ***")
        print("Daily Price Data:")
        pprint(built_stock.daily_price_data)
        print("-----------------")
        print("Stories:")
        for story in built_stock.news:
            print(story.title)
            print(story.publisher)
            print(datetime.fromtimestamp(story.published_timestamp))
            print(story.link)
            print("-----------------")
        print("")
        print("")

if __name__ == "__main__":
    main()
