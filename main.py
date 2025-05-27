from dotenv import load_dotenv
import utils, csv, os, websockets, asyncio, json
from datetime import datetime, timezone
from models import init_db

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# create a logs folder if its not there

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)


# for every file execution create a new log file in the logs folder.
timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
log_filename = os.path.join(log_dir, f"log-{timestamp}.csv")

with open(log_filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["timestamp", "payload_obj"])
    writer.writeheader()

# getting 5 instruments
options = utils.fetch_options_by_expiry()[:5]
instruments = [option['instrument_name'] for option in options]
instruments.append("ticker.BTC-PERPETUAL.raw")
print(instruments)




async def main():
    conn = init_db()
    cursor = conn.cursor()

    url = "wss://test.deribit.com/ws/api/v2"
    async with websockets.connect(url) as ws:
        # Authenticate
        auth_msg = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "public/auth",
            "params": {
                "grant_type": "client_credentials",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET
            }
        }
        await ws.send(json.dumps(auth_msg))
        auth_resp = await ws.recv()
        print("✅ Authenticated:", auth_resp)

        # Subscribe to BTC-PERPETUAL ticker
        sub_msg = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "public/subscribe",
            "params": {
                "channels": ["ticker.BTC-PERPETUAL.raw"]
            }
        }
        await ws.send(json.dumps(sub_msg))
        sub_resp = await ws.recv()
        print("📡 Subscribed:", sub_resp)

        print("\n📈 Live BTC-PERPETUAL Ticker Updates:")
        while True:
            ts_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            message = await ws.recv()
            data = json.loads(message)
            with open(log_filename, mode='a', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=["timestamp", "payload_obj"])
                        writer.writerow({
                                        "timestamp": ts_str,
                                        "payload_obj": json.dumps(data)
                                    })

            if data.get("method") == "subscription" and "params" in data:
                channel = data["params"]["channel"]  # e.g. ticker.BTC-PERPETUAL.raw
                ticker = data["params"]["data"]
                ts = ticker["timestamp"]

                instrument = channel.split('.')[1]  # extract instrument name

                # Extract required fields safely
                price = ticker.get("last_price")
                volatility = ticker.get("iv")
                delta = ticker.get("delta")

                # Insert into DB
                cursor.execute("""
                    INSERT INTO ticker_data (instrument, price, volatility, delta, timestamp)
                    VALUES (?, ?, ?, ?, ?)
                """, (instrument, price, volatility, delta, ts))
                conn.commit()

                # Print confirmation
                print(f"[{datetime.utcfromtimestamp(ts/1000)} UTC] Stored: {instrument}, price={price}, iv={volatility}, delta={delta}")

if __name__ == "__main__":
    asyncio.run(main())