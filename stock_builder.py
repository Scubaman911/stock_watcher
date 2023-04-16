"""
Builder pattern for the YFinance Ticker.
"""

"""
Stocks
-> Contains:
- News 
"""
import yfinance as yf
from abc import ABC, abstractmethod
from typing import Any

from stock_data import StockData, DailyPriceData, News

class StockBuilder():
    """
    Concrete builder for the Stock class.
    """
    def __init__(self, ticker: str) -> None:
        self.ticker = yf.Ticker(ticker)
        self.ticker_str = ticker # for reset
        self.reset()

    def reset(self) -> None:
        self._stock = Stock(self.ticker_str)

    @property
    def stock(self):
        stock = self._stock
        self.reset()
        return stock
    
    def collate_daily_price_data(self) -> None: 
        info = self.ticker.info
        daily_prices = DailyPriceData(
            current_price=info.get("currentPrice"),
            open_price=info.get("open"),
            previous_close_price=info.get("previousClose"),
        )
        self._stock.daily_price_data = daily_prices

    def collate_news_data(self):
        news = self.ticker.news
        


class Stock():
    def __init__(self, ticker: str) -> None:
        self.ticker = ticker
        self._data = StockData()

    @property
    def daily_price_data(self):
        return self._data.daily_price_data
    
    @daily_price_data.setter
    def daily_price_data(self, daily_price_data: DailyPriceData):
        self._data.daily_price_data = daily_price_data

    @property
    def news(self):
        return self._data.news
    
    @news.setter
    def news(self, news: News):
        self._data.news = news
        
    