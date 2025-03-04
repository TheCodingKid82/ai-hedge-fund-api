"""
Lightweight version of the backtester for Vercel deployment.
This version uses minimal dependencies and simplified functionality.
"""
import json
import datetime
from typing import Callable, List, Dict, Any

class BacktesterLite:
    """A lightweight version of the Backtester class for deployment"""
    
    def __init__(
        self,
        agent: Callable,
        tickers: list[str],
        start_date: str,
        end_date: str,
        initial_capital: float,
        model_name: str = "gpt-4o",
        model_provider: str = "OpenAI",
        selected_analysts: list[str] = [],
        initial_margin_requirement: float = 0.0,
    ):
        self.agent = agent
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.initial_capital = initial_capital
        self.model_name = model_name
        self.model_provider = model_provider
        self.selected_analysts = selected_analysts
        self.initial_margin_requirement = initial_margin_requirement
        
        # Initialize portfolio
        self.portfolio = {ticker: 0 for ticker in tickers}
        self.cash = initial_capital
        self.portfolio_values = []
        
    def run_backtest(self):
        """
        Simplified backtest that returns a basic response instead of running a full simulation
        """
        # For deployment, we'll return a simplified response
        # In a real implementation, you would fetch data and run the simulation
        
        response = {
            "message": "Backtest request received and will be processed asynchronously",
            "parameters": {
                "tickers": self.tickers,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "initial_capital": self.initial_capital,
                "model": self.model_name,
                "provider": self.model_provider,
                "analysts": self.selected_analysts
            },
            "status": "queued"
        }
        
        return response
        
    def analyze_performance(self):
        """
        Return simplified performance metrics
        """
        return {
            "message": "Performance analysis will be generated after backtest completion",
            "status": "pending"
        } 