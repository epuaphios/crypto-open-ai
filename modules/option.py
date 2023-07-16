from rich.console import Console
console = Console()
from modules.investment_recommendation import get_investment_recommendation
def user_option(coin,coin_data, eth_data, coin_opens, coin_highs, coin_lows, coin_closes, eth_opens, eth_highs, eth_lows, eth_closes, gpt_api, days, option):
    investment_recommendation = get_investment_recommendation(coin, coin_data, eth_data, coin_opens, coin_highs, coin_lows, coin_closes, eth_opens, eth_highs, eth_lows, eth_closes, gpt_api, option)

    print("\nInvestment Recommendation:", investment_recommendation)
    return