from flask import Flask, request, jsonify
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Simplified portfolio_management_agent function for Vercel deployment
def portfolio_management_agent(*args, **kwargs):
    return "This is a simplified agent for Vercel deployment"

# Simplified backtester for Vercel deployment
class BacktesterLite:
    def __init__(self, agent, tickers, start_date, end_date, initial_capital, **kwargs):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.initial_capital = initial_capital
        self.kwargs = kwargs
    
    def run_backtest(self):
        return {
            "message": "Backtest request received",
            "parameters": {
                "tickers": self.tickers,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "initial_capital": self.initial_capital,
                **self.kwargs
            },
            "status": "processed",
            "note": "This is a lightweight API deployment. For full functionality, please run the application locally."
        }
    
    def analyze_performance(self):
        return {
            "message": "Performance analysis in lightweight version",
            "note": "This is a simplified API deployed on Vercel. For full functionality, please run the application locally.",
            "example_metrics": {
                "sharpe_ratio": 1.5,
                "max_drawdown": -0.15,
                "total_return": 0.25
            }
        }

# Simplified run_hedge_fund function for Vercel
def run_hedge_fund(tickers, start_date, end_date, **kwargs):
    return {
        "message": "Hedge fund analysis request received",
        "parameters": {
            "tickers": tickers,
            "start_date": start_date,
            "end_date": end_date,
            **kwargs
        },
        "status": "processed",
        "note": "This is a lightweight API deployment. For full functionality, please run the application locally."
    }

@app.route('/')
def home():
    return jsonify({"status": "success", "message": "AI Hedge Fund API is running"})

@app.route('/api/backtest', methods=['POST'])
def backtest():
    try:
        data = request.json
        
        # Validate required parameters
        required_params = ['tickers', 'start_date', 'end_date', 'initial_capital']
        for param in required_params:
            if param not in data:
                return jsonify({"status": "error", "message": f"Missing required parameter: {param}"}), 400
        
        # Extract parameters with defaults
        tickers = data['tickers']
        start_date = data['start_date']
        end_date = data['end_date']
        initial_capital = float(data['initial_capital'])
        model_name = data.get('model_name', 'gpt-4o')
        model_provider = data.get('model_provider', 'OpenAI')
        selected_analysts = data.get('selected_analysts', [])
        initial_margin_requirement = float(data.get('initial_margin_requirement', 0.0))
        
        # Create Backtester instance
        backtester = BacktesterLite(
            agent=portfolio_management_agent,
            tickers=tickers,
            start_date=start_date,
            end_date=end_date,
            initial_capital=initial_capital,
            model_name=model_name,
            model_provider=model_provider,
            selected_analysts=selected_analysts,
            initial_margin_requirement=initial_margin_requirement
        )
        
        # Run the backtest
        results = backtester.run_backtest()
        performance = backtester.analyze_performance()
        
        # Combine results
        response = {
            "status": "success",
            "backtest_results": results,
            "performance_metrics": performance
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/hedge-fund', methods=['POST'])
def hedge_fund():
    try:
        data = request.json
        
        # Validate required parameters
        required_params = ['tickers', 'start_date', 'end_date']
        for param in required_params:
            if param not in data:
                return jsonify({"status": "error", "message": f"Missing required parameter: {param}"}), 400
        
        # Extract parameters with defaults
        tickers = data['tickers']
        start_date = data['start_date']
        end_date = data['end_date']
        portfolio = data.get('portfolio', {})
        show_reasoning = data.get('show_reasoning', False)
        selected_analysts = data.get('selected_analysts', [])
        model_name = data.get('model_name', 'gpt-4o')
        model_provider = data.get('model_provider', 'OpenAI')
        
        # Run hedge fund
        results = run_hedge_fund(
            tickers=tickers,
            start_date=start_date,
            end_date=end_date,
            portfolio=portfolio,
            show_reasoning=show_reasoning,
            selected_analysts=selected_analysts,
            model_name=model_name,
            model_provider=model_provider
        )
        
        return jsonify({"status": "success", "results": results})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# This is required for Vercel serverless deployment
# The variable name 'app' is what Vercel looks for by default