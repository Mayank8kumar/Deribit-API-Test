import requests


def fetch_options_by_expiry(target_expiry=""):
    url = "https://www.deribit.com/api/v2/public/get_instruments"
    params = {
        "kind": "option",
        "expired": "false"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        instruments = response.json()['result']
        filtered = [inst for inst in instruments if target_expiry in inst['instrument_name']]
        return filtered
    else:
        print(f"Error: {response.status_code}")
        return []