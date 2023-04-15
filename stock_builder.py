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
    def __init__(self, ticker) -> None:
        self.ticker = ticker
        self.reset(ticker)

    def reset(self, ticker) -> None:
        
        self._stock = Stock(ticker)

    @property
    def stock(self):
        stock = self._stock
        self.reset(self.ticker)
        return stock
    
    def get_daily_price_data():



class Stock():
    def __init__(self, ticker: str) -> None:
        self.ticker = ticker
        self._data = StockData()

    @property
    def daily_price_data(self):
        return self._data.daily_price_data()
    
    @daily_price_data.setter
    def daily_price_data(self, daily_price_data: DailyPriceData):
        self._data.daily_price_data = daily_price_data

    @property
    def news(self):
        return self._data.news()
    
    @news.setter
    def news(self, news: News):
        self._data.news = news
        
    