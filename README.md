# Deribit Options Ticker Subscriber

This project connects to the **Deribit Testnet WebSocket API**, authenticates using your API credentials, subscribes to live ticker updates for BTC perpetual and selected option instruments, stores key data in a SQLite database, and logs raw messages in timestamped CSV files.

---

## ✅ Setup Instructions

1. **Clone or download this repository**

2. **Create a Python virtual environment (recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required packages:**

```bash
pip install -r requirements.txt
```

4. **Set your Deribit Testnet API credentials:**

Create a `.env` file in the root directory with the following:

```env
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here
```

*You can obtain testnet credentials from the Deribit developer portal.*

---

## ▶ How to Run the Script

Run the main script to:

* Connect to Deribit WebSocket
* Authenticate
* Subscribe to BTC-PERPETUAL and 5 options
* Log raw payloads
* Store select data to SQLite

```bash
python main.py
```

---

## 📌 Example Output

```bash
['BTC-27MAY22-40000-C', 'BTC-27MAY22-42000-C', 'BTC-27MAY22-43000-C', 'BTC-27MAY22-44000-C', 'BTC-27MAY22-45000-C', 'ticker.BTC-PERPETUAL.raw']
✅ Authenticated: {"jsonrpc":"2.0","id":1,"result":{...}}
📡 Subscribed: {"jsonrpc":"2.0","id":2,"result":null}
📈 Live BTC-PERPETUAL Ticker Updates:
[2025-05-28 12:34:56 UTC] Stored: BTC-PERPETUAL, price=30500, iv=0.75, delta=0.45
[2025-05-28 12:34:57 UTC] Stored: BTC-PERPETUAL, price=30502, iv=0.76, delta=0.46
...
```

---

## 🗂 How to View Stored Data

Run the `view_data.py` script to print the last 10 records stored in the SQLite database:

```bash
python view_data.py
```

### Example Output

```
** Here Are The Last 10 records:- **

2025-05-28 12:34:57 UTC | Instrument: BTC-PERPETUAL | Price: 30502 | IV: 0.76 | Delta: 0.46
2025-05-28 12:34:56 UTC | Instrument: BTC-PERPETUAL | Price: 30500 | IV: 0.75 | Delta: 0.45
...
```

---

## 🧾 Project Structure

```
.
├── main.py          # Main WebSocket client with auth, subscription, DB + CSV logging
├── view_data.py     # Helper to view last 10 DB entries
├── models.py        # SQLite DB schema setup
├── utils.py         # Helper to fetch Deribit option instruments
├── .env             # (not included) API credentials
├── logs/            # Auto-created folder for storing CSV logs
└── deribit_tickers.db # SQLite DB file (auto-created)
```

---
