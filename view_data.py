import sqlite3
from datetime import datetime, timezone


# this prints the last 10 records inserted in the db.

def view_data():
    
    conn = sqlite3.connect("deribit_tickers.db")
    cursor = conn.cursor()

    cursor.execute("SELECT instrument, price, volatility, delta, timestamp FROM ticker_data ORDER BY timestamp DESC LIMIT 10")
    rows = cursor.fetchall()
    print("\n\n ** Here Are The Last !0 records:- ** \n")
    for instrument, price, iv, delta, ts in rows:
        ts_str = datetime.fromtimestamp(ts / 1000, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{ts_str} UTC | Instrument: {instrument} | Price: {price} | IV: {iv} | Delta: {delta}")

    conn.close()

view_data()