import sqlite3

def init_db():
    conn = sqlite3.connect("deribit_tickers.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS ticker_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            instrument TEXT,
            price REAL,
            volatility REAL,
            delta REAL,
            timestamp INTEGER
        )
    """)
    conn.commit()
    return conn



