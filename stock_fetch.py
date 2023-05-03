from typing import List
from pprint import pprint
from stock_builder import StockBuilder, Stock
from stock_tickers import ticker_list
from stock_utils import percentage_change, on_schedule
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import logging

@on_schedule
def collate_stocks():
    stocks: List[Stock] = []
    with ThreadPoolExecutor(max_workers=16) as executor:
        for result in executor.map(build_stock, ticker_list):
            stocks.append(result)


def build_stock(stock):
    built = StockBuilder(stock)
    built.collate_daily_price_data()
    built.collate_news_data()
    logging.info(f"*** Info collated for {built.ticker}! ***")
    return built.stock



def main():
    logging.info("Stock Watcher Started!")
    collate_stocks()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, 
        format= '[%(asctime)s] %(levelname)s - %(message)s')
    main()


# TO SEE STUFF
# logging.info(f"*** Info for {built_stock.ticker}! ***")
# logging.info("Daily Price Data:")
# pprint(built_stock.daily_price_data)
# pcnt = percentage_change(built_stock.daily_price_data.current_price, built_stock.daily_price_data.open_price)
# logging.info(f"PERCENTAGE CHANGE: {pcnt:.2f}%")
# logging.info("-----------------")
# logging.info("Stories:")
# for story in built_stock.news:
#    logging.info(story.title)
#    logging.info(story.publisher)
#    logging.info(datetime.fromtimestamp(story.published_timestamp))
#    logging.info(story.link)
#    logging.info("-----------------")
# logging.info("")
# logging.info("")
