# AI Hedge Fund API

A Flask API for running AI agents and backtests for algorithmic trading.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up environment variables by copying `.env.example` to `.env` and filling in your API keys:
   ```
   cp .env.example .env
   ```

3. Run the server:
   ```
   python server.py
   ```

The server will start on port 5000 by default, or you can set the `PORT` environment variable.

## API Endpoints

### 1. Home
- **URL**: `/`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "status": "success",
    "message": "AI Hedge Fund API is running"
  }
  ```

### 2. Run Backtest
- **URL**: `/api/backtest`
- **Method**: `POST`
- **Parameters**:
  ```json
  {
    "tickers": ["AAPL", "MSFT", "GOOGL"],
    "start_date": "2023-01-01",
    "end_date": "2023-12-31",
    "initial_capital": 100000,
    "model_name": "gpt-4o",
    "model_provider": "OpenAI",
    "selected_analysts": ["warren_buffett", "portfolio_manager"],
    "initial_margin_requirement": 0.0
  }
  ```
- **Required Parameters**: `tickers`, `start_date`, `end_date`, `initial_capital`
- **Response**:
  ```json
  {
    "status": "success",
    "backtest_results": { ... },
    "performance_metrics": { ... }
  }
  ```

### 3. Run Hedge Fund
- **URL**: `/api/hedge-fund`
- **Method**: `POST`
- **Parameters**:
  ```json
  {
    "tickers": ["AAPL", "MSFT", "GOOGL"],
    "start_date": "2023-01-01",
    "end_date": "2023-12-31",
    "portfolio": {},
    "show_reasoning": false,
    "selected_analysts": ["warren_buffett", "portfolio_manager"],
    "model_name": "gpt-4o",
    "model_provider": "OpenAI"
  }
  ```
- **Required Parameters**: `tickers`, `start_date`, `end_date`
- **Response**:
  ```json
  {
    "status": "success",
    "results": { ... }
  }
  ```

## Available Analysts

- `fundamentals` - Fundamental analysis agent
- `technicals` - Technical analysis agent
- `sentiment` - Sentiment analysis agent
- `valuation` - Valuation analysis agent
- `portfolio_manager` - Portfolio management agent
- `risk_manager` - Risk management agent
- `warren_buffett` - Warren Buffett strategy agent
- `ben_graham` - Benjamin Graham strategy agent
- `bill_ackman` - Bill Ackman strategy agent

## Sample cURL Commands

### Running a Backtest
```bash
curl -X POST http://localhost:5000/api/backtest \
  -H "Content-Type: application/json" \
  -d '{
    "tickers": ["AAPL", "MSFT", "GOOGL"],
    "start_date": "2023-01-01",
    "end_date": "2023-12-31",
    "initial_capital": 100000,
    "model_name": "gpt-4o",
    "selected_analysts": ["warren_buffett", "portfolio_manager"]
  }'
```

### Running the Hedge Fund
```bash
curl -X POST http://localhost:5000/api/hedge-fund \
  -H "Content-Type: application/json" \
  -d '{
    "tickers": ["AAPL", "MSFT", "GOOGL"],
    "start_date": "2023-01-01",
    "end_date": "2023-12-31",
    "show_reasoning": true,
    "selected_analysts": ["fundamentals", "technicals", "portfolio_manager"]
  }'
``` 