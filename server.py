from api.index import app
import os
from dotenv import load_dotenv
if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=port, debug=True) 