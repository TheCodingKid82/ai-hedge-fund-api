"""
Minimal version of the backtester for Vercel deployment.
Uses only standard libraries and minimal dependencies.
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
        
        # Initialize basic portfolio
        self.portfolio = {ticker: 0 for ticker in tickers}
        self.cash = initial_capital
        
    def run_backtest(self):
        """
        Simplified backtest that returns a status message
        """
        # For deployment, we just acknowledge receipt of the request
        timestamp = datetime.datetime.now().isoformat()
        
        response = {
            "message": "Backtest request received",
            "timestamp": timestamp,
            "parameters": {
                "tickers": self.tickers,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "initial_capital": self.initial_capital,
                "model": self.model_name,
                "provider": self.model_provider,
                "analysts": self.selected_analysts
            },
            "status": "processed",
            "note": "This is a lightweight API. For full backtesting functionality, please run the application locally."
        }
        
        return response
        
    def analyze_performance(self):
        """
        Return simplified performance metrics
        """
        return {
            "message": "Performance analysis in lightweight version",
            "note": "This is a simplified API deployed on Vercel. For full functionality, please run the application locally.",
            "example_metrics": {
                "sharpe_ratio": 1.5,
                "max_drawdown": -0.15,
                "total_return": 0.25
            }
        } 