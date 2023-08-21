import requests

def get_historical_data(product_id, api_url, start_date, end_date):
    candles_url = f"{api_url}/{product_id}/candles"
    params = {
        "start": start_date.isoformat(),
        "end": end_date.isoformat(),
        "granularity": 3600,
    }
    response = requests.get(candles_url, params=params)
    data = response.json()
    return data


def get_historical_order(product_id, api_url):
    candles_url = f"{api_url}/{product_id}/book?level=2"
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.get(candles_url, headers=headers)
    data = response.json()
    return data