from typing import Dict, List, Optional
import yfinance as yf
from pprint import pprint
from stock_builder import Stock
# currentPrice
# open
# previousClose

ticker_list = ["RIO.L", "RIVN", "^FTSE"]

# class DataHelper():
#     @staticmethod
#     def tickers_to_daily_price_data(tickers: List[str]):
#         subjects = yf.Tickers(tickers)

#         data_models = {}
#         for ticker, data in subjects.tickers.items():
#             data_models[ticker] = DailyPriceData(
#                 current_price=data.info.get("currentPrice"),
#                 open_price=data.info.get("open"),
#                 previous_close_price=data.info.get("previousClose")
#             )
#             pprint(f"Created: {data_models[ticker]}")
#         return data_models


def main():
    pass   
    

if __name__ == "__main__":
    main()
