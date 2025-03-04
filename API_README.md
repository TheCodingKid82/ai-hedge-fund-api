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

## Deployment to Vercel

This API is optimized for deployment to Vercel. Due to Vercel's serverless function size limitations (250MB), we've created a lightweight version for deployment.

### Deployment Steps

1. Push your code to GitHub
2. Connect your GitHub repository to Vercel
3. Configure the deployment:
   - Build Command: `pip install -r requirements.txt`
   - Output Directory: `.`
   - Install Command: `pip install -r requirements.txt`

### Local vs. Deployed Functionality

The deployed version on Vercel uses a lightweight implementation that:
- Returns immediate responses for API calls
- Queues actual processing to be done asynchronously
- Avoids heavy dependencies like pandas and matplotlib

For full functionality with real-time processing, run the API locally using:
```bash
pip install -r requirements-dev.txt
python server.py
```

### Troubleshooting Vercel Deployment

If you encounter deployment issues:

1. **Function Size Limit**: Ensure you're using the lightweight requirements.txt
2. **Function Count Limit**: Make sure vercel.json is configured to use only api/index.py
3. **Dependencies**: Check that all dependencies in requirements.txt are compatible with Vercel's environment

For production use cases requiring full functionality, consider:
- Using a different hosting provider (Heroku, DigitalOcean, AWS)
- Implementing a queue-based architecture with separate worker processes
- Splitting the application into microservices 