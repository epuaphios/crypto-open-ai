import requests
def get_current_price(product_id, headers):
    url = f"https://api.coinbase.com/v2/prices/{product_id}/spot"
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['data']['amount']