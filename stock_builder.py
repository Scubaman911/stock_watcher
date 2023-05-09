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
from typing import Any, List, Optional
import json
from attr import asdict

from stock_data import StockData, DailyPriceData, NewsStory

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
        self.ticker.info # pull information

    @property
    def stock(self):
        stock = self._stock
        self.reset()
        return stock
    
    def collate_daily_price_data(self) -> None: 
        info = self.ticker.info
        daily_prices = DailyPriceData(
            currency=info.get("currency"),
            current_price=info.get("currentPrice"),
            open_price=info.get("open"),
            previous_close_price=info.get("previousClose"),
        )
        self._stock.daily_price_data = daily_prices

    def collate_news_data(self):
        news = self.ticker.news

        if type(news) == list:
            stories = []
            story: dict
            for story in news:
                element = NewsStory(
                    title=story.get("title"),
                    published_timestamp=story.get("providerPublishTime"),
                    publisher=story.get("publisher"),
                    link=story.get("link")
                )
                stories.append(element)
            self._stock.news = stories

    def collate_ticker_identifiers(self):
        info = self.ticker.info
        self._stock.symbol = info.get("underlyingSymbol")
        self._stock.long_name = info.get("longName")

class Stock():
    def __init__(self, ticker: str) -> None:
        self.ticker = ticker
        self._data = StockData()

    @property
    def daily_price_data(self) -> DailyPriceData:
        return self._data.daily_price_data
    
    @daily_price_data.setter
    def daily_price_data(self, daily_price_data: DailyPriceData):
        self._data.daily_price_data = daily_price_data

    @property
    def news(self) -> List[NewsStory]:
        return self._data.news_stories
    
    @news.setter
    def news(self, news: List[NewsStory]):
        self._data.news_stories = news
        
    @property
    def symbol(self) -> str:
        return self._data.symbol
    
    @symbol.setter
    def symbol(self, symbol: str):
        self._data.symbol = symbol

    @property
    def long_name(self) -> str:
        return self._data.long_name
    
    @long_name.setter
    def long_name(self, long_name: str):
        self._data.long_name = long_name

    def to_json(self):
        return json.dumps(asdict(self._data))