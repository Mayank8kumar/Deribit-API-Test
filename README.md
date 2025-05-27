# Deribit Options Ticker Subscriber

This project connects to the Deribit Testnet WebSocket API, authenticates using your API credentials, subscribes to live ticker updates for options and perpetual instruments, stores key data in a SQLite database, and provides a simple way to view recent stored ticker data.

---

## Setup Instructions

1. **Clone or download this repository** to your local machine.

2. **Create a Python virtual environment (recommended):**

`
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
`

Install required packages:

`
pip install -r requirements.txt
`
Set your Deribit Testnet API credentials:

Create a .env file in the root directory with:

`
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here
(You can get testnet credentials from Deribit API portal)
`

How to Run the Script
Run the main script to start the WebSocket client, authenticate, subscribe to tickers, and store data:

`
python main.py
`
The script will:

Authenticate with Deribit Testnet

Subscribe to BTC-PERPETUAL ticker and 5 options (fetched dynamically)

Store ticker updates (instrument, price, volatility, delta, timestamp) in SQLite DB (deribit_tickers.db)

Print confirmation of stored data live

Example Output

`
['BTC-27MAY22-40000-C', 'BTC-27MAY22-42000-C', 'BTC-27MAY22-43000-C', 'BTC-27MAY22-44000-C', 'BTC-27MAY22-45000-C', 'ticker.BTC-PERPETUAL.raw']
✅ Authenticated: {"jsonrpc":"2.0","id":1,"result":{...}}
📡 Subscribed: {"jsonrpc":"2.0","id":2,"result":null}
📈 Live BTC-PERPETUAL Ticker Updates:
[2025-05-28 12:34:56 UTC] Stored: BTC-PERPETUAL, price=30500, iv=0.75, delta=0.45
[2025-05-28 12:34:57 UTC] Stored: BTC-PERPETUAL, price=30502, iv=0.76, delta=0.46
...

`
How to View Stored Data
Run the view_data.py script to print the last 10 records stored in the SQLite database:

`
python view_data.py
`
Example output:


 ** Here Are The Last 10 records:- ** 

2025-05-28 12:34:57 UTC | Instrument: BTC-PERPETUAL | Price: 30502 | IV: 0.76 | Delta: 0.46
2025-05-28 12:34:56 UTC | Instrument: BTC-PERPETUAL | Price: 30500 | IV: 0.75 | Delta: 0.45
...

** End of Last 10 Records **

Project Structure
main.py — Main async script to connect, authenticate, subscribe, and store ticker data

models.py — Database initialization and schema

utils.py — Helper to fetch options instruments from Deribit API

view_data.py — Script to query and print recent stored data

.env — Your API credentials (not included in repo for security)

