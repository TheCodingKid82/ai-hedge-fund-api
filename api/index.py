from flask import Flask, request, jsonify
from api.backtester import Backtester
from api.main import run_hedge_fund
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

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
        
        # Create Backtester instance with the agent function
        from api.agents.portfolio_manager import portfolio_management_agent
        
        backtester = Backtester(
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