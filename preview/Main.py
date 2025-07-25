import yfinance as yf
from fastmcp import Component

class NewsComponent(Component):
    def forward(self, ticker: str):
        stock = yf.Ticker(ticker.upper())
        news = stock.news[:5]
        return [
            {
                "title": item["title"],
                "publisher": item.get("publisher", "Unknown"),
                "link": item["link"]
            }
            for item in news
        ]
