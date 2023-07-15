import requests
import json
import datetime
import matplotlib.pyplot as plt
from modules.investment_recommendation import get_investment_recommendation
from modules.historical_getter import get_historical_data
from modules.current_price  import get_current_price
from rich.console import Console
from modules.option import user_option

console = Console()

with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()
headers = {
    "CB-ACCESS-KEY": api_key,
}

with open('gpt_api.txt', 'r') as file:
    gpt_api = file.read().strip()



def get_prices(coin, days, option):

    coin_usd_price = get_current_price(coin+"-USD", headers)
    eth_usd_price = get_current_price("ETH-USD", headers)
    # Print current prices
    print(coin+"-USD price:", coin_usd_price)
    print("ETH-USD price:", eth_usd_price)


    api_url = "https://api.pro.coinbase.com/products"


    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(int(days))


    coin_data = get_historical_data(coin+"-USD", api_url, start_date, end_date)
    coin_timestamps = [datetime.datetime.fromtimestamp(int(entry[0])) for entry in coin_data]
    coin_opens = [entry[3] for entry in coin_data]
    coin_highs = [entry[2] for entry in coin_data]
    coin_lows = [entry[1] for entry in coin_data]
    coin_closes = [entry[4] for entry in coin_data]


    eth_data = get_historical_data("ETH-USD", api_url, start_date, end_date)
    eth_timestamps = [datetime.datetime.fromtimestamp(int(entry[0])) for entry in eth_data]
    eth_opens = [entry[3] for entry in eth_data]
    eth_highs = [entry[2] for entry in eth_data]
    eth_lows = [entry[1] for entry in eth_data]
    eth_closes = [entry[4] for entry in eth_data]
    user_option(coin,coin_data, eth_data, coin_opens, coin_highs, coin_lows, coin_closes, eth_opens, eth_highs, eth_lows, eth_closes,gpt_api, days, option)
    show_plot(coin_timestamps, coin_closes, coin_lows, coin_highs, eth_timestamps, eth_closes, eth_lows, eth_highs, days)

def show_plot(coin_timestamps, coin_closes, coin_lows, coin_highs, eth_timestamps, eth_closes, eth_lows, eth_highs, days):

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    ax1.plot(coin_timestamps, coin_closes, color='blue')
    ax1.vlines(coin_timestamps, coin_lows, coin_highs, color='black', linewidth=1)
    ax1.set_title(f"Bitcoin (coin-USD) - {days} Day Historical Data")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Price (USD)")
    ax2.plot(eth_timestamps, eth_closes, color='green')
    ax2.vlines(eth_timestamps, eth_lows, eth_highs, color='black', linewidth=1)
    ax2.set_title(f"Ethereum (ETH-USD) - {days} Day Historical Data")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Price (USD)")
    fig.autofmt_xdate()  
    plt.tight_layout()
    plt.show()

def get_option(coin, days, option):
    get_prices(coin, days, option)
   
