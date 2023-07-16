import requests

def get_historical_data(product_id, api_url, start_date, end_date):
    candles_url = f"{api_url}/{product_id}/candles"
    params = {
        "start": start_date.isoformat(),
        "end": end_date.isoformat(),
        "granularity": 86400, 
    }
    response = requests.get(candles_url, params=params)
    data = response.json()
    return data